# Case 4: Bed load transport

## Physical settings
- Channel geometry:
    - Widening open channel, 50 m long, 0.01 bed slope
    - Upstream width: 20 m; downstream width: 40 m
    - Initial bed: dry, fixed for first 100 s, then mobile
    - Uniform bed material: grain size 0.02 m, density 3000 kg/m³, porosity 0.4
    - Schematic diagram: ![Schematic_04](/04_bedloadtransport/Physics/Schematic.jpg)
- Flow scenario:
    - Stationary flow with 20 m³/s discharge
    - Morphological change simulated after 100 s

## Numerical settings
- Computational mesh: 231 unstructured triangular cells. Visualization: ![Meshing_04](/04_bedloadtransport/Physics/meshing.jpg)
- Simulation performed with BASEHPC on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P)
- Simulation time: 500 s physical time

## Input files:
- **model.json**: configuration file specifying physical problem and numerical settings, including the computational mesh (.2dm file). BASEMENT writes its info into a setup.h5 file, which is used for simulation.
- **widening_open_channel.2dm**: unstructured triangular mesh file required by BASEHPC as computational domain. For .2dm file format, see [SMS wiki](https://www.xmswiki.com/wiki/SMS:2D_Mesh_Files_*.2dm?__cf_chl_tk=r_woYILHa12UMY664uxq5gFDzTZfQia_Lz7.6bShzj8-1759226996-1.0.1.1-1aZOLNVb_EeD1zsV.on53xi.Jr71gmBhP2pD1xdBYy0). This file was generated using the script **widening_open_channel.py** adapted from the usage_example.py at [BASEmesh repo](https://gitlab.ethz.ch/vaw/public/basemesh-v2/-/tree/master/examples/meshtool?ref_type=heads). 

- **simulation.json**: configuration file specifying numerical settings, variables to store, and time intervals for storing. Used with setup.h5 to launch computation.
- **results.json**: configuration file for converting results.h5 to .xdmf for visualization. The .xdmf file references results.h5 and does not store data itself.
- The .json files can be edited directly for fine-tuning and rerunning simulations.

## Computation statistics:
- Unstructured triangular mesh of 2380 cells solved on 16 CPU threads using BASEHPC.
- CPU model: 12th Gen Intel(R) Core(TM) i7-1260P.
- cpu-time = 3.13 s for 500 s physical time.

## Post-processing & visualization:
- The .psvd file in /ParaView stores the pipeline for loading, processing, and visualizing data (.xdmf and .h5 files). Open this file in ParaView after simulation.
- Animation of water surface and bed elevation (3D view): ![Animation_04_3D](/04_bedloadtransport/ParaView/04_bedloadtransport_3Dview.gif)
- Animation of water surface and bed elevation (2D profile along channel central line): ![Animation_04_2D](/04_bedloadtransport/ParaView/04_bedloadtransport_2Dview.gif)
