# This code returns intact molecule 
from schrodinger.structure import StructureReader, StructureWriter
from schrodinger.application.matsci import clusterstruct
from schrodinger.application.matsci.nano.xtal import ( 
        PBC_POSITION_KEY, ANCHOR_PBC_POSITION, translate_to_cell, 
        connect_atoms) 
import sys
import os

def main():
    fnames = sys.argv[1:]
    base, ext = os.path.basename(fnames[0]).split(os.path.extsep, maxsplit=1)

    structs = []
    for st in fnames:
        structs.extend(StructureReader(st))

    for st in structs: 
        st.property[PBC_POSITION_KEY] = ANCHOR_PBC_POSITION % ('0', '0', '0') 
        translate_to_cell(st)

    for st in structs:
        connect_atoms(st, pbc_bonding=True)

    """    
    # make molecules intact / unwrap molecules 
    # needed for deduplication or rmsd_n calculations 
    # contract_by_molecule does i) unwrap molecule and 
    # ii) aligns box center with structure center
    # contract_by_molecule2 is more robust but does not do (ii)	  
    """    
    structs_unwrap = []
    for st in structs:
        clusterstruct.contract_by_molecule(st)
        structs_unwrap.append(st)

    structs = structs_unwrap.copy()

    fout = base + "." + ext
    with StructureWriter(fout) as writer:
        writer.extend(structs)

if __name__ == '__main__':
    main()
