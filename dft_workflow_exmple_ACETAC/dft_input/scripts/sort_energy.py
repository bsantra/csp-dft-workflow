# This code sorts the mae or maegz files according to ENERGY_KEY
from schrodinger.structure import StructureReader, StructureWriter
from schrodinger.utils.units import KCAL_PER_MOL_PER_HARTREE
import numpy as np
import sys
import os
import argparse

'''
The following two properties will be added to output mae
'''
ENERGY_PER_MOLECULE_KEY = "r_matsci_DFT_energy_per_molecule"
RELATIVE_ENERGY_PER_MOLECULE_KEY = "r_matsci_Relative_DFT_energy_per_molecule_(kcal/mol)"

def parse_args():

    parser = argparse.ArgumentParser(
        description='''Sorts the mae or maegz files according to energy per molecule
        New proprty added: r_matsci_DFT_energy_per_molecule,
        New proprty added: r_matsci_Relative_DFT_energy_per_molecule_(kcal/mol)''',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "input_mae", type=str,
        help = "input list of structures in mae format",
    )

    parser.add_argument(
        "-e", "--energy_window", type=float, default=4.0,
        help = "energy window to retain structures in kcal/mol",
    )

    parser.add_argument(
        "-n", "--n_thresh", type=int, default=300,
        help = "threshold for number of structures to retain",
    )

    parser.add_argument(
        "--energy_key", type=str, default="r_matsci_Etot_(Ry)",
        help = "property key that holds the energy of the supercell",
    )
    parser.add_argument(
        "-o", "--outname", default=None,
        help = "name of the output file, if None will append -filtered to input name",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    energy_window = args.energy_window
    n_thresh = args.n_thresh
    if args.outname is None:
        base, ext = os.path.basename(args.input_mae).split(os.path.extsep, maxsplit=1)
        outname = str(base) + "-filtered." + str(ext)
        print(base,ext,outname)
    else:
        outname = args.outname
        base, ext = os.path.basename(outname).split(os.path.extsep, maxsplit=1)

    structs = []
    structs.extend(StructureReader(args.input_mae))

    for st in structs:
        # factor 0.5 to convert from Rydberg to Hartree
        st.property[ENERGY_PER_MOLECULE_KEY] = st.property[args.energy_key] / st.mol_total * 0.5

    energy = []
    for n, st in enumerate(structs):
        energy.append(st.property[ENERGY_PER_MOLECULE_KEY])

    min_energy = min(energy)
    for n, st in enumerate(structs):
        energy[n] -= min_energy
        energy[n] *= KCAL_PER_MOL_PER_HARTREE

    for n, st in enumerate(structs):
        st.property[RELATIVE_ENERGY_PER_MOLECULE_KEY] = energy[n]

    structs_sorted = sorted(structs, key=lambda st: st.property[RELATIVE_ENERGY_PER_MOLECULE_KEY])

    structs = structs_sorted.copy()

    outfile = []
    for n, st in enumerate(structs):
        if st.property[RELATIVE_ENERGY_PER_MOLECULE_KEY] < energy_window:
            if n < n_thresh:
                outfile.append(st)

    print("number of initial structures:", len(structs))
    print("maximum relative energy: %6.2f" % max(energy), "kcal/mol")
    #print("number of structures within ", energy_window, " kcal/mol:", len(outfile))

    with StructureWriter(outname) as writer:
        writer.extend(outfile)

    with open(base + "-relative-energy.csv", "w") as fout:
        print("title", RELATIVE_ENERGY_PER_MOLECULE_KEY, file=fout)
        for st in structs:
            print(st.title,str(st.property[RELATIVE_ENERGY_PER_MOLECULE_KEY]),file=fout)


if __name__ == '__main__':
    main()
