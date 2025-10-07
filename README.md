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

Computation statistics are based on an unstructured triangular mesh of 8,727 cells, solved using BASEHPC on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P), with a total CPU time of 256.512 seconds for 110 seconds of simulated physical time. For comparison, the total CPU time is 505.452 seconds when using 2 CPU threads.

The water depth and velocity vector field form t = 0 to 110 s looks like 
![Animation_01](/01_openchannelflow/ParaView/01_openchannelflow.gif)
![Animation_01](/01_openchannelflow/ParaView/01_openchannelflow.gif)

### Case 2: Dam break

This case simulates the sudden failure of a dam, resulting in rapid downstream flooding. The domain consists of a flat rectangular channel 15 m long and 1 m wide, with an initial water level of 10 m upstream of the dam and a dry bed downstream. ![Schematic_02](/02_dambreak/Physics/Schematic.jpg) Both the up- and downstream boundaries are treated as vertical walls.
This case simulates the sudden failure of a dam, resulting in rapid downstream flooding. The domain consists of a flat rectangular channel 15 m long and 1 m wide, with an initial water level of 10 m upstream of the dam and a dry bed downstream. ![Schematic_02](/02_dambreak/Physics/Schematic.jpg) Both the up- and downstream boundaries are treated as vertical walls.

The computational mesh uses 231 unstructured triangular cells (see below). ![Meshing_02](/02_dambreak/Physics/meshing.jpg) The simulation is performed with BASEHPC on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P), requiring only 0.075 seconds of CPU time for 10 seconds of simulated physical time. 
The computational mesh uses 231 unstructured triangular cells (see below). ![Meshing_02](/02_dambreak/Physics/meshing.jpg) The simulation is performed with BASEHPC on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P), requiring only 0.075 seconds of CPU time for 10 seconds of simulated physical time. 

The simulated water surface and velocity look like:
![Animation_02](/02_dambreak/ParaView/02_dambreak.gif)
![Animation_02](/02_dambreak/ParaView/02_dambreak.gif)

### Case 3: Malpasset dam break

This case reproduces the H_BP_4 case documented in the Testcases.pdf shipped with BASEMENT. This hydraulic test case benefits from the well known real world dataset from the Malpasset dam break in France. The complex geometry, high velocities, often and sudden wet-dry changes and the good documentation allow for a fundamental evaluation of the hydraulic code.

The Malpasset dam was a doubly-curved equal angle arch type with variable radius. It breached on December 2nd, 1959 all of a sudden. The entire wall collapsed nearly completely what makes this event unique. The breach created a water flood wall 40 meters high and moving at 70 km/h. After 20 minutes, the flood reached the village Frejus and still had 3 m depth. The time of the breach and the flood wave can be exactly reconstructed, as the time is known, when the power of different stations switched off.

### Case 4: Bed load transport

This case tests the bed load transport and morphological modules in BASEHPC. The senario of stationary flow in a widening open channel is simulated. It is expected that as the channel widens and the flow decelerates, the bed load transport decreases downstream and thus the bed elevates due to accretion. 

Specifically, the channel increases from 20 m wide at the upstream inflow boundary to be 40 m wide at the outflow boundary 50 m downstream. ![Schematic_04](/04_bedloadtransport/Physics/Schematic.jpg) The model was initialised with 20 m<sup>3</sup>/s discharge and a dry bed, which was set to be fixed bed in the first 100 seconds. After that the bed load transport module was activated and accordingly the morphological change was simulated. A uniform bed of grain size 0.02 m, density 3000 kg/m<sup>3</sup> and porosity 0.4 was adopted. The bed load transport was computed using the Meyer-Peter and Müller (1948) model (see MPM model in the reference manuals for details of the mathematical model implemented in the sediment transport module of BASEMENT).

The computational mesh uses 2380 unstructured triangular cells ![Meshing_04](/04_bedloadtransport/Physics/meshing.jpg) The simulation is performed with BASEHPC on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P), requiring 3.13 seconds of CPU time for 500 seconds of simulated physical time. 

Shown below are the 3D view of water surface and bed elevation ![Animation_04_3D](/04_bedloadtransport/ParaView/04_bedloadtransport_3Dview.gif) as well as the 2D profile along the channel central line. ![Animation_04_2D](/04_bedloadtransport/ParaView/04_bedloadtransport_2Dview.gif)
