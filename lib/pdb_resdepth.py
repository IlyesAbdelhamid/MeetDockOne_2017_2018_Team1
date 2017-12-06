#!/usr/bin/env python3

from Bio.PDB import *
import os

def calculate_resdepth(structure, pdb_filename):
    '''Takes as argument a structure object for parsing and a pdb file.
        Returns a dictionnary containing a key (tuple) composed of the
        chain, three letter code and position in chain of a given residue;
        and its value which is the residue depth.
    '''
    model = structure[0]
    rd = ResidueDepth(model, pdb_filename)
    mydict = {}

    for item in rd.property_list:

        # Create a tuple => (chain, residue3LetterCode, Id)
        residue = (
                    item[0].get_parent().id,    # Chain
                    item[0].get_resname(),      # 3 letter code
                    item[0].get_id()[1]         # Position in chain
                )
        result = item[1]                        # (ResidueDepth, CalphaDepth)



        # Stores everything in a dict

        mydict[residue] = result

    return mydict

def bfactor_to_resdepth(mydict):
    '''Takes as argument the dictionnary containing residue depth for
       a given residue.
       Edit the bfactor column of a pdb file which is replaced with
       the residue depth of the corresponding residue (calculated in
       the function calculate_resdepth.
    '''

    with open('2za4.pdb', 'r') as input:
        with open('2za4_modified.pdb', 'w') as output:
            for line in input:
                if not line.startswith("HETATM"):
                    if line.startswith("ATOM"):
                        _chain = line[21:22].strip()
                        _code = line[17:20].strip()
                        _id = int(line[22:26].strip())
                        values = mydict[(_chain, _code, _id)]
                        edited_line = "{}{:6.2f}{}".format(line[:60], values[0], line[66:])
                        output.write(edited_line)
                    else:
                        output.write(line)



def delete_hetatm(pdb_filename):
    ''' Takes as argument a pdb file.
        Removes HETATM lines.
    '''
    command = "grep -v 'HETATM' {} > clean_{}".format(pdb_filename, pdb_filename)
    os.system(command)

def resdepth_to_fft(residue, cutoff, mydict):

    res = (residue.get_parent().id, # Chain
           residue.get_resname(),   # 3 letter code
           residue.get_id()[1]      # Position in chain
          )
    if mydict[res][0] < cutoff:        # test on ResidueDepth
        return(1)
    else:
        return(9j)

if __name__=='__main__':
    delete_hetatm("2za4.pdb")
    dico_res = calculate_resdepth('clean_2za4.pdb')
    bfactor_to_resdepth(dico_res)
    resdepth_to_fft('D', 'SER', 89, 4, dico_res)