# Case 2: Open channel flow

## Physical settings
- Channel geometry:
    - Flat rectangular channel, 15 m long and 1 m wide
    - Initial water level: 10 m upstream of the dam, dry bed downstream. Schematic diagram of the domain ![Schematic](/02_dambreak/Physics/Schematic.jpg)
    - Both upstream and downstream boundaries are vertical walls
- Flow scenario:
    - Sudden dam failure, causing rapid downstream flooding

## Numerical settings
- Computational mesh: 231 unstructured triangular cells. Visualization of the computational mesh ![Meshing](/02_dambreak/Physics/meshing.jpg)
- Simulation performed with BASEHPC on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P)
- Simulation time: 10 s physical time

## Input files:
- **model.json**: configuration file that specifies physical problem and some numerical settings, including the computational mesh .2dm file. BASEMENT **DOES NOT** directly use this file to run simulation but by default write its info into a setup.h5 file first, which was actually used later to execute simulation.
- **two_region_basin.2dm**: unstructured triangular mesh file required by BASEHPC as computational domain. For definition of the .2dm file format please see [this web by SMS](https://www.xmswiki.com/wiki/SMS:2D_Mesh_Files_*.2dm?__cf_chl_tk=r_woYILHa12UMY664uxq5gFDzTZfQia_Lz7.6bShzj8-1759226996-1.0.1.1-1aZOLNVb_EeD1zsV.on53xi.Jr71gmBhP2pD1xdBYy0). The .2dm file used here was generated using the script **two_region_basin.py** adapted from the usage_example.py at [BASEmesh repo](https://gitlab.ethz.ch/vaw/public/basemesh-v2/-/tree/master/examples/basechange?ref_type=heads). 
- **simulation.json**: configuration file that specifies:
  - Numerical settings controlling the computation process (e.g., time step).
  - What variables to store and the time interval for storing. 
    
    BASEMENT takes this file together with the setup.h5 file generated from **model.json** as input to launch the computation.
- **results.json**: configuration file that specifies converting the results.h5 file (generated during simulation) into a .xdmf file. Technically it's not right to say 'convert' since the .xdmf file does not really store any data and must always be used with results.h5 placing in the same folder.
- The .json configuration files were initially populated using the GUI provided. This is convenient to get started but not so much in the later fine tuning and debugging steps when you repeatedly tuning parameters and re-run the simulation. In the later case it's better to simply edit the .json file directly and call the BASEMENT executables in a terminal environment.

## Computation statistics:
- Unstructured triangular mesh of 231 cells solved on 16 CPU threads using BASEHPC.
- CPU model: 12th Gen Intel(R) Core(TM) i7-1260P.
- cpu-time = 0.075 s for 10 s physical time.

## Post-processing & visualization:
- The .psvd file in /ParaView stores the pipeline of loading, processing and visualising data (.xdmf and the .h5 files in this case). After finish simulation simply opening this file in your ParaView.
- The animation of water depth and velocity vector field form t = 0 to 10 s is saved in /ParaView folder as the .mp4 file and looks like below
![Animation_02_dambreak](/02_dambreak/ParaView/02_dambreak.gif)