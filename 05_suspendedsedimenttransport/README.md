# Case 5: Suspended sediment transport

## Physical settings
- Channel geometry:
    - Using same mesh as case 04 (widening open channel)
    - Channel length: 50 m
    - Upstream width: 20 m; downstream width: 40 m
    - Inflow boundary slope: 0.05
    - Outflow boundary slope: 0.01
    - Manning coefficient: 0.035 s/m<sup>1/3</sup>
- Flow scenario:
    - Stationary flow with 20 m³/s discharge
    - Initially dry bed
- Sediment properties:
    - Grain size: 0.005 m (5 mm)
    - Sediment density: 2650 kg/m³
    - Sediment porosity: 0.4
    - Critical Shields parameter: 0.02

## Numerical settings
- Hydraulic parameters:
    - CFL number: 0.9
- Morphological parameters:
    - Fixed bed for first 100 s, then morphodynamic
    - Bedload transport:  
        - Bedload was specified in model.json only formally by artificially setting its pre-factor to zero. This is to demonstrate the morphological change solely induced by erosion of suspended sediment (i.e. bed materials being picked up by water flow).
    - Suspended load:
        - Initial condition: zero concentration
        - Erosion rate: van Rijn closure model
        - Deposition rate: lin's model with the coefficient tuned down to m = 0.8 to weaken the deposition and encourage bed erosion for demo purpose
        - Relaxation parameter: default value 0.1 (related with the numerical solver (Vanzo et al., 2016) for computing the solution of the diffusive terms, see [Section 2.5.2](https://people.ee.ethz.ch/~basement/baseweb/download/documentation/BMdoc_Reference_Manual_BASEHPC_v4-1-0.pdf#page=70) in reference manual)
        - Beta factor: 1.0: the $\beta_s$ calibration factor for the erosion rate $q_e=w_s \beta_s C_r$ ($w_s$ = settling velocity, $C_r$ = reference concentration, see [Section 1.3.2.1](https://people.ee.ethz.ch/~basement/baseweb/download/documentation/BMdoc_Reference_Manual_BASEHPC_v4-1-0.pdf#page=46) in reference manual)

## Input files:
- **model.json**: configuration file specifying physical problem and numerical settings, including the computational mesh (.2dm file). BASEMENT writes its info into a setup.h5 file, which is used for simulation.
- **widening_open_channel.2dm**: unstructured triangular mesh file required by BASEHPC as computational domain. For .2dm file format, see [SMS wiki](https://www.xmswiki.com/wiki/SMS:2D_Mesh_Files_*.2dm). This file is the same as used in case 04.
- **simulation.json**: configuration file specifying numerical settings, variables to store, and time intervals for storing. Used with setup.h5 to launch computation.
- **results.json**: configuration file for converting results.h5 to .xdmf for visualization. The .xdmf file references results.h5 and does not store data itself.
- The .json files can be edited directly for fine-tuning and rerunning simulations.

## Computation statistics:
- Unstructured triangular mesh of 2380 cells (same as case 04)
- CPU model: 12th Gen Intel(R) Core(TM) i7-1260P
- Solved using BASEHPC on 16 CPU threads with 3.13 seconds cpu-time for 400 seconds physical time simulation

## Post-processing & visualization:
- The .psvd file in /ParaView stores the pipeline for loading, processing, and visualizing data (.xdmf and .h5 files). Open this file in ParaView after simulation.
- Visualizations include:
    - Water surface elevation
    - Suspended sediment concentration
    - Bed elevation changes
![Animation_05](/05_suspendedsedimenttransport/ParaView/05_suspendedsedimenttransport.gif)