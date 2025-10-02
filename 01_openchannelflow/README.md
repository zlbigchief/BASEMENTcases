# Case 1: Open channel flow

## Physical settings:
- Channel geometry:
  - Trapezoidal cross-sectional shape of 20 m bottom width, 60 m top width and 10 m height
  - Horizontal length 450 m
  - Bed slope 0.05
  - Manning friction coefficient 0.05 s/m<sup>1/3</sup>
- Flow parameters: 
  - Incoming discharge 1558 m<sup>3</sup>/s

To help design and verify the simulation results, a python script ComputeFr.py is provided in /Physics to compute average streamwise velocity and Frounde number based on the physical settings provided using the Manning formula.

## Numerical settings:
- Initially filled the domain with 5 m deep water with 0.5 m/s downstream velocity
- Inflow discharge condition specified at right boundary (x = 450 m)
- Free outflow condition specified at left boundary (x = 0 m)
- Total simulation time 110 s, results output at 10 s interval
- Dynamic time step according to CFL number limit of 0.9
- Unstructured triangular mesh solved on 16 CPU threads using BASEHPC

## Input files:
- **model.json**: configuration file that specifies physical problem and some numerical settings, including the computational mesh .2dm file. BASEMENT **DOES NOT** directly use this file to run simulation but by default write its info into a setup.h5 file first, which was actually used later to execute simulation.
- **trapezoidal_channel_mesh.2dm**: unstructured triangular mesh file required by BASEHPC as computational domain. For definition of the .2dm file format please see [this web by SMS](https://www.xmswiki.com/wiki/SMS:2D_Mesh_Files_*.2dm?__cf_chl_tk=r_woYILHa12UMY664uxq5gFDzTZfQia_Lz7.6bShzj8-1759226996-1.0.1.1-1aZOLNVb_EeD1zsV.on53xi.Jr71gmBhP2pD1xdBYy0). This .2dm file used was initially generated using the script **trapezoidal_channel.py** from the [BASEmesh repo](https://gitlab.ethz.ch/vaw/public/basemesh-v2/-/tree/master/examples/basechange?ref_type=heads). It was later edited manually to add a few key lines needed for defining boundary and initial conditions according to the manual.
- **simulation.json**: configuration file that specifies:
  - Numerical settings controlling the computation process (e.g., time step).
  - What variables to store and the time interval for storing. 
    
    BASEMENT takes this file together with the setup.h5 file generated from **model.json** as input to launch the computation.
- **results.json**: configuration file that specifies converting the results.h5 file (generated during simulation) into a .xdmf file. Technically it's not right to say 'convert' since the .xdmf file does not really store any data and must always be used with results.h5 placing in the same folder.

## Computation statistics:
- Unstructured triangular mesh of 8727 cells solved on 16 CPU threads using BASEHPC.
- CPU model: 12th Gen Intel(R) Core(TM) i7-1260P.
- cpu-time = 256.512s for 110 s physical time.

## Post-processing & visualization:
- The .psvd file in /ParaView stores the pipeline of loading, processing and visualising data (.xdmf and the .h5 files in this case). After finish simulation simply opening this file in your ParaView.
- The animation of water depth and velocity vector field form t = 0 to 110 s is saved in /ParaView folder as the .mp4 file and looks like below
![Animation_01_openchannelflow](/01_openchannelflow/ParaView/01_openchannelflow.gif)