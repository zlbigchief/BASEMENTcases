# BASEMENTcases

This project will be my self-tutorial courses for learning how to use [BASEMENT v4.1](https://basement.ethz.ch/download/software-download.html) and postprocessing results in ParaView or QGIS. I try to set up, run and postprocessing a few cases. Each case will be stored with its own scripts for pre- and post-processing and input files.

## About BASEMENT:
The software system BASEMENT(BAsic-Simulation-EnvironMENT) is a software developed at VAW of ETH Zurich for simulating river flow, sediment transport and other material transports, harnessing the parallel computation of CPU/GPU hybrid architecture. The software provides a functional environment for numerical simulation of river flows with sediment transport in alpine and sub-alpine regions. The main focus of conception and development is the robustness of the numerical models, the flexibility of the computational grid and the combination and efficiency of the method of calculation (problem dependent equations, coupling of models, parallelization).

## Simulation cases and file structure

### Case 1: Open channel flow

Physical settings:

- Channel geometry:
  - Trapezoidal cross-sectional shape of 20 m bottom width, 60 m top width and 10 m height
  - Horizontal length 450 m
  - Bed slope 0.05
  - Manning friction coefficient 0.05 s/m<sup>1/3</sup>
- Flow parameters: 
  - Incoming discharge 1558 m<sup>3</sup>/s

Numerical settings:

- Initially filled the domain with 5 m deep water with 0.5 m/s downstream velocity
- Inflow discharge condition specified at right boundary (x = 450 m)
- Free outflow condition specified at left boundary (x = 0 m)
- Total simulation time 110 s, results output at 10 s interval
- Dynamic time step according to CFL number limit of 0.9
- Unstructured triangular mesh solved on 16 CPU threads using BASEHPC

Input files:

- **model.json**: configuration file that specifies physical problem and some numerical settings, including the computational mesh .2dm file. BASEMENT **DOES NOT** directly use this file to run simulation but by default write its info into a setup.h5 file for later use to execute simulation.
- **simulation.json**: configuration file that specifies:
  - Numerical settings controlling the computation process (e.g., time step).
  - What variables to store and the time interval for storing. 
    
    BASEMENT takes this file together with the setup.h5 file generated from **model.json** as input to launch the computation.

- **results.json**: configuration file that specifies converting the results.h5 file (generated during simulation) into a .xdmf file. Technically it's not right to say 'convert' since the .xdmf file does not really store any data and must always be used with results.h5 placing in the same folder.

Post-processing & visualization:
