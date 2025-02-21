import matplotlib.pyplot as plt
from chem1d_utilities import *
import numpy as np

# Read chem1d data
yiend = readchem1d("../exercise1/yiend.dat")

# Put spatial coordinate in array x
x = yiend.var('x(i)')

# Computing the mass burning
ik  = np.argmax(yiend.var('HeatRel'))
phi = yiend.var('Massflow')
mbr = (phi[ik]-phi[ik-1])/(x[ik+1]-x[ik-1])*(x[ik]-x[ik-1])+phi[ik-1];

print('Flame temperature: {:.6e} K'.format(yiend.var('Temp')[-1][0]))
print('Mass burning rate: {:.6e} gr/(cm2s)'.format(mbr))
print('Burning velocity : {:.6e} cm/s'.format(yiend.var('Massflow')[0][0] / yiend.var('Density')[0][0]))
print('CO emission      : {:.6e}'.format(yiend.var('CO')[-1][0]))
print('NO emission      : {:.6e}'.format(yiend.var('NO')[-1][0]))

# Plot T vs x
plt.figure(1)
plt.plot(x, yiend.var('Temp'), '.-', label='Temperature')
plt.xlabel('x [cm]')
plt.ylabel('T [K]')
plt.title('Temperature vs x')
plt.grid(True)

# Plot species mass fractions vs x
species_names = ['CH4', 'O2', 'CO2', 'H2O', 'CO', 'OH', 'NO']

plt.figure(2)
for species_name in species_names:
    plt.plot(x, yiend.var(species_name), '.-', label=species_name)  # Adjust indexing if needed
plt.xlabel('x [cm]')
plt.ylabel('Mass fraction [-]')
plt.title('Species Mass Fractions vs x')
plt.legend()
plt.grid(True)

# Uncomment for log scale:
# plt.yscale('log')
# plt.ylim([1e-8, 1])

# Plot NO mass fraction vs x
plt.figure(3)
plt.plot(x,yiend.var('NO'), '.-', label='NO')
plt.xlabel('x [cm]')
plt.ylabel('NO mass fraction [-]')
plt.title('NO Mass Fraction vs x')
plt.grid(True)

# Plot Massflow vs x
plt.figure(4)
plt.plot(x,yiend.var('Massflow'), '.-', label='Massflow')
plt.xlabel('x [cm]')
plt.ylabel('Massflow [gr/cm^2s]')
plt.title('Massflow vs x')
plt.grid(True)

plt.show()