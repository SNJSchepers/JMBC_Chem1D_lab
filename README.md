# JMBC Chem1D Practical

This repository includes Chem1D executables for Windows and Linux, exercise setups, and post-processing routines for MATLAB and Python.

## Setting up and running `chem1d`

**1. Clone this repository and go into directory.**
```
git clone https://github.com/SNJSchepers/JMBC_Chem1D_lab.git
cd JMBC_Chem1D_lab
```
This directory contains several exercise directories which each contain Chem1D input and output files. The input files, `settings.csf` and `defaults.csf` are ascii text files containing keywords and values, which are the settings used to control the code.

**2. Enter the** `exercise1` **directory and open both input files (**`.csf`**) using your favorate text editor (e.g. Notepad, WordPad, vim, nano, etc.).**

Chem1D works by first reading the `defaults.csf` and subsequently reading `settings.csf` overwriting the default settings. If you want to change a default setting, copy the lines from  `defaults.csf` to `settings.csf` and change the values. Do **not** change anything in `defaults.csf`.

**3. Copy the executable corresponding to your OS (Windows or Linux) to the** `exercise1` **directory and execute.**

The screen output of the code is also written in the `chem1d.log`. In this file you can check whether the solver has found a converged solution. Some results such as burning velocity and flame temperature are listed at the end of this file. The solution (species mass fractions, temperature, velocity, etc. for each position $x$) is stored in the file `yiend.dat`. The data (e.g. species profiles) can be visualised using MATLAB or Python. 

**If you want to use MATLAB for post processing**

**4. Go into the** `post_processing\matlab` **directory and use the** `plotexample.m` **MATLAB script to visualise the profiles.**

**If you want to use Python for post processing**

**4. Go into the** `post_processing\python ` **directory, create a virtual environment and install the requirements.**

Windows (CMD):
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Linux:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You can use the same environment for all the exercises. As long as you don’t run `deactivate`, there’s no need to repeat this step for each exercise.  

**5. Run** `plotexample.py` **to visualise the profiles.**
```
python plotexample.py
```

## Exercise 1: Premixed methane-air flames
Compute a stoichiometric premixed flame using the initial unchanged settings. Take a look at the temperature and species profiles and try to understand/explain them. Is the computational domain large enough? Are you using enough grid points?

### 1.1 Stoichiometry and emissions

Now change the stoichiometry $\phi$ of the flame by changing the first entry under `[BOUNDARY_EQUIVALENCERATIO]` in `settings.csf` from `1.00` to `0.95`. Leave the second entry on the line unchanged. Analyze the results; focuss on the burning velocity $s_L$ and flame temperature $T_b$. 

Now, use the same procedure to compute flames for a range of $\phi = 0.6-1.3$. Chem1D detects if there is already an `yiend.dat` file in the case folder and uses that as an initial starting point. Therefore, if the solver does not converge within 1000 iterations, terminate the program and apply a smaller step in $\phi$. Store the solution (`yiend.dat`) files into a folder using clear naming (e.g. `mixav\yiend_phi094.dat`).

Plot $s_L$ and $T_b$ against $\phi$ for your range. The flame temperature $T_b$ is the temperature of the burnt gas and can be found at the last grid point. Next, create a plot of CO and NO emissions against equivalence ratio $\phi$. The CO and NO emissions may be represented as the mass fractions of
the species at the last grid point of the domain.

### 1.2 Burning velocity: Temperature and pressure dependence

For this exercise, you will investigate the dependence of burning velocity on temperature and pressure. The pressure can be varied by changing the value under `[BOUNDARY_INLETPRESSURE]`. Plot $s_L/s_L^0$ against $p/p^0$, where the superscript $^0$ indicates the reference value at standard conditions. How does the burning velocity scale with pressure. How does the burning velocity change with pressure? What about the mass burning rate $\rho_us_L/(\rho_us_L)^0$?

Do the same for the inlet temperature $T_u$. Increase it with several steps from 300 to 500 K by changing the value under `[BOUNDARY_INLETTEMPERATURE]`. Note that there are two temperature entries: the first corresponds to the fuel, and the second to the oxidizer stream. However, since this is a premixed case, both should have the same values. Plot log($s_L$) as a function of $1/T_b$ and compute the activation energy $E_a$ from the slope of this curve. 

Another way to change the flame temperature $T_b$ is by varying the amount of nitrogen dilution. If you decrease the amount of N$_2$ in the oxidizer, the flame temperature will increase and vice versa. Try this and compare with the variations in $T_u$. Do you find the same $s_L$ for the same $T_b$? What about the mass burning rate $m = \rho_u s_L$?

### 1.3 Simplified transport: Constant Lewis numbers

When using Chem1D, the species diffusion is by default modeled using mixture-averaged diffusion coefficients. We want to know what the effect is of assuming constant Lewis numbers. To do that, we first need to determine the Lewis numbers. Luckily, Chem1D can do this for us. It fits constant values to the mixture-averaged coefficients, which vary with $x$. Run Chem1D with the option `LEWIS` under `[POSTPROCESSING_OUTPUTFILES]` in `settings.csf` turned `ON`. An additionally output file, `lewis.dat`, will be generated containing the Lewis numbers of all species. Try this. 

We can use these Lewis numbers directly in the transport equation of species by changing the transport model `[MODEL_TRANSPORT]` to `LEWIS`. Make sure that the name of the Lewis number file is set correctly to `lewis.dat` at `[LEWIS_TRANSPORTFILE]`. Chem1D will read the Lewis numbers from this file and use them to compute the species diffusion coefficients. Compute a stoichiometric flame and compare the results with the mixture-averaged model. 

In many theoretical and numerical models, unity Lewis numbers are assumed for all species ($\text{Le}_i = 1$ for all $i$). Chem1D automatically sets the Lewis number of a species to 1 if it can not be found in the `lewis.dat` file. Therefore, to enforce unity Lewis coefficients for all species, remove the old lewis.dat file and create a new empty file called `lewis.dat`. Determine the laminar burning velocity $s_L$ and $T_b$ and compare it with the other two diffusion models. Also, take a look at the enthalpy profile. What do you notice?

## 2 Non-premixed counterflow flames

Compute a non-premixed counterflow flame with the default settings in the directory `exercise2`. Take a look at the species and temperature profiles and try to understand/explain them. Also plot the species and temperature profiles as function of the mixture fraction (`MixFrac`).

### 2.1 Strain rate and quenching

Change the strain rate $a$ of the flame by changing `[STRAINANDCURVATURE_STRAIN]` in `settings.csf` from 162 to 170 1/s. Run Chem1D and analyse the results. Compare the profiles with the previous run. 

Increase the strain rate in small steps until the solver can not find a steady solution. At that point the flame quenches. Plot $T_\text{max}$ against $a$. 

### 2.2 Dilution

Dilute the fuel stream with nitrogen. What do you expect in terms of the flame temperature and stoichiometric mixture fraction? What happens when you dilute the oxidizer?

### 2.3 Preheating and auto-ignition

Now you will study the effect of preheating. What happens with flame temperature and NO emissions when you preheat the fuel and what happens when you preheat the oxidizer to 500 K?

If the temperature of the reactants is high enough, the mixture will auto-ignite. This is an unsteady process, which needs an initial solution and a time integration method. The initial solution can be created by solving a steady problem with frozen chemistry, i.e. $\omega_i = 0$. You can achieve this by setting `[MODEL_CHEMISTRY]` to `FROZEN` and run Chem1D. Then set the chemistry model back to detailed and run a time-dependent simulation with this frozen-chemistry solution as initial point. Try this for a methane-air case with an air temperature of 1400 K. The time evolution of some variables (including the maximum temperature) is recorded in a text file called `fort.67`. This file can be imported in Matlab for visuualization. 

## 3 Lean premixed stretched flames

Flame stretch has an important effect on the burning velocity of premixed flames. To investigate this, you will compute some stretched premixed flames. Enter the `exercise3` directory and compute a lean methane-air flmae with an equivalence ratio of $\phi = 0.6$. Record the mass burning rate $m^0$ given at the end of the log file. Now apply a constant stretch rate $K$ by setting the option `[STRAINANDCURVATURE_STRAIN] to 50 1/s. What happens to the mass burning rate? 

Continue this procedure to $a=200$ 1/s and plot the scaled mass burning rate $m/m^0$ as a function of the dimensionless stretch rate $\text{Ka} = al_F^0/s_L^0$. Here denotes $l_F$ the laminar flame thickness, which can also be found at the end of the log file. The superscript $^0$ denotes the unstretched case. Note that the slope of this curve corresponds to the Markstein number Ma,

$\frac{m}{m^0} = 1 - \text{Ma}\text{Ka} + \text{h.o.t.}$

Repeat this exercise for a methane-hydrogen (60%-40%) fuel mixture. What do you observe for the Markstein number? What does this mean for the (planar) stability of the flame?










