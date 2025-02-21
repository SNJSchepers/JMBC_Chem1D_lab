import numpy as np
import os

# ------------------------------ Auxiliary classes and functions ------------------------------
class chem1d_array():
    def __init__(self, names, data, t=0):
        self.names = names
        self.data = data
        self.time = t

    def var(self, name):
        return self.data[:, self.names == name]
        
def listStruc(Struc=None,fieldname=None):
    return [Struc[x][fieldname] for x in range(len(Struc))]
    
def SpInd(Name,Sp):
    return listStruc(Sp,"Name").index(Name)

def ElInd(Name,El):
    return listStruc(El,"Name").index(Name)
    
  
def readchem1d(fname):
    fid = open(fname, "r")
    i = 0
    t = 0
    while True:
        line = fid.readline()
        i += 1
        if (line == ""):
            break
        elif ("[TIME]" in line):
            line = fid.readline()
            i += 1
            t = float(line)
        elif ("[FILE_STRUCTURE_COLUMNS_CONTAINING]" in line):
            line = fid.readline()
            i += 1
            a = np.array(line.split())
            y = np.loadtxt(fname, dtype=float, skiprows=i)
    data = chem1d_array(a, y, t)
    return data

def writechem1d(fname,y, t, a, Sp, Nk):
    if not Nk:
        Nk = np.size(y,0)
    Nsp = len(Sp)
    Nvar = len(a)
    if not t:
        t = 0.000000000000000E+00

    file = open(fname, 'w')
    
    file.write('[CHEM1D_DATAFILE_VERSION]\n4\n\n[NUMBER_OF_GRIDPOINTS]\n'+str(Nk)+'\n')
    file.write('[MOLE_OR_MASS_FRACTIONS]\n MASS\n')
    file.write('[NUMBER_OF_SPECIES]\n'+str(Nsp)+'\n')
    file.write('[NUMBER_OF_VARIABLES]\n'+str(Nvar-2)+'\n')
    file.write('[TIME]\n'+str(t)+'\n')
    file.write('[FILE_STRUCTURE_COLUMNS_CONTAINING]\n')
    
    file.write(' '.join(a)+'\n')
    for k in range(Nk):
        ystr = []
        for i in range(Nvar):
            if i == 0:
                ystr.append(str(round(y[k,i])))
            else:
                ystr.append(str(y[k,i]))
        #ystr = [str(y[k,i]) for i in range(len(y[k,:]))]
        file.write(' '.join(ystr)+'\n')

