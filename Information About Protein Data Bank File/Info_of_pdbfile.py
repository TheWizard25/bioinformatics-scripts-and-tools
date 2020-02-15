import sys
from Bio.PDB import *
pdbinput = sys.argv[1]
pdboutput=sys.argv[2]
parser = PDBParser(PERMISSIVE=1)         # creating a PDBParser object
structure = parser.get_structure('self', pdbinput)  #create a structure object from a PDB file
with open(pdboutput, 'w') as f:
    print("TITLE - ",structure.header['name'], file=f)   
    print(" ",file=f)
    print("HEAD - ",structure.header['head'], file=f)
    print(" ",file=f)
    print("KEYWORD - ",structure.header['keywords'], file=f)
    print(" ",file=f)
    print("Deposition Date -",structure.header['deposition_date'], file=f)
    print(" ",file=f)
    print("Realease Date -",structure.header['release_date'], file=f)
    print(" ",file=f)
    print("Structure method -",structure.header['structure_method'], file=f)
    print(" ",file=f)
    print("Structure reference -",structure.header['structure_reference'], file=f)   #(maps to a list of references)
    print(" ",file=f)
    print("Journal Reference -",structure.header['journal_reference'], file=f)
    print(" ",file=f)
    print("Author -",structure.header['author'], file=f)
    print(" ",file=f)
    print("Journal Reference -",structure.header['journal_reference'], file=f)
    print(" ",file=f)
    print("Compound -",structure.header['compound'], file=f)    # (maps to a dictionary with various information about the crystallized compound).
    print(" ",file=f)
    print("HEADER -",structure.header, file=f)


