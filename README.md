# BASEMENTcases

This project will be my self-tutorial courses for learning how to use [BASEMENT v4.1](https://basement.ethz.ch/download/software-download.html) and postprocessing results in ParaView or QGIS. I try to set up, run and postprocessing a few cases. Each case will be stored with its own scripts for pre- and post-processing and input files.

## About BASEMENT:
The software system BASEMENT(BAsic-Simulation-EnvironMENT) is a software developed at VAW of ETH Zurich for simulating river flow, sediment transport and other material transports, harnessing the parallel computation of CPU/GPU hybrid architecture. The software provides a functional environment for numerical simulation of river flows with sediment transport in alpine and sub-alpine regions. The main focus of conception and development is the robustness of the numerical models, the flexibility of the computational grid and the combination and efficiency of the method of calculation (problem dependent equations, coupling of models, parallelization).

There are a few manuals and documents coming together with the software after installation:
- **Intro and installation**: how to install BASEMENT for Windows and Linux systems and release notes of latest features and changes in recent versions
- **User manual**: describing the modelling environment of BASEMENT (particularly the super user-friendly GUI), including the three stages of pre-processing, simulation and postprocessing.
- **Reference manual BASEMD**: information about the mathematical models and numerical approximations in BASEMD module
- **Reference manual BASEHPC**: information about the mathematical models and numerical approximations in BASEHPC module
- **Tutorials**: Guidance on how to use BASEmesh and how to postprocessing results using QGIS and ParaView; Step-by-step guides on how to set up realistic cases
- **Testcases**: collection of common benchmark cases for testing hydrodynamic, sediment and vegetation modules; domain coupling and high-performance computation
- Appendix:

## Simulation cases and file structure
Below are introductions of the physical settings, computational stats and quick views of the results. For detailed documentations of each case please see the README.md in each case folder.

### Case 1: Open channel flow

The physical settings for this case include a trapezoidal channel geometry with a bottom width of 20 m, top width of 60 m, and height of 10 m, extending horizontally for 450 m with a bed slope of 0.05 and a Manning friction coefficient of 0.05 s/m<sup>1/3</sup>. The flow parameters feature an incoming discharge of 1558 m<sup>3</sup>/s. 

Computation statistics are based on an unstructured triangular mesh of 8,727 cells, solved using BASEHPC on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P), with a total CPU time of 256.512 seconds for 110 seconds of simulated physical time.

The water depth and velocity vector field form t = 0 to 110 s looks like 
![Animation_01_openchannelflow](/01_openchannelflow/ParaView/01_openchannelflow.gif)
