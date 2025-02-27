# This code renames title 
from schrodinger.structure import StructureReader, StructureWriter
from schrodinger.application.matsci.nano.xtal import connect_atoms
import sys
import os
import argparse

def parse_args():

    parser = argparse.ArgumentParser(
        description='''rename title''',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "inmae", type=str, help = "input list of structures in mae format",
    )
    parser.add_argument("-ni", type=int, default=1, help = "index of first character")
    parser.add_argument("-nf", type=int, default=5, help = "index of last character")

    return parser.parse_args()

def main():
    args = parse_args()
    base, ext = os.path.basename(args.inmae).split(os.path.extsep, maxsplit=1)

    structs = []
    structs.extend(StructureReader(args.inmae))

    ni = args.ni; nf = args.nf 
    for st in structs:
        title = st.title.split("_", -1)
        if (len(title) != nf ):
            for n in range(ni, nf + 1):
                if n == ni:
                    st.title = f"{title[n]}"
                else:
                    st.title += f"_{title[n]}"
#       print(st.title)

#   for st in structs:
#       connect_atoms(st, pbc_bonding=True)

    fout = base + "." + ext
    with StructureWriter(fout) as writer:
        writer.extend(structs)

if __name__ == '__main__':
    main()
