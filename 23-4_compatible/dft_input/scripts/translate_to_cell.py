import sys
import os 

from schrodinger.structure import StructureReader, StructureWriter
from schrodinger.application.matsci.nano.xtal import ( 
        CENTER_PBC_POSITION, PBC_POSITION_KEY, 
        ANCHOR_PBC_POSITION, translate_to_cell) 

fnames = sys.argv[1:]
base, ext = os.path.basename(fnames[0]).split(os.path.extsep, maxsplit=1)

structs = []
for st in fnames:
    structs.extend(StructureReader(st))
    
for st in structs: 
#   st.property[PBC_POSITION_KEY] = CENTER_PBC_POSITION
    st.property[PBC_POSITION_KEY] = ANCHOR_PBC_POSITION % ('0', '0', '0') 
    translate_to_cell(st)

#fout = base + "_in_cell." + ext
fout = base + "." + ext
with StructureWriter(fout) as writer:
    writer.extend(structs)
