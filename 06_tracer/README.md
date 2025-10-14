# Case 6: Conservative tracer transport

## Physical settings
- **Geometry**: identical trapezoidal channel as Case 1, 450 m long with 20 m bottom width, 60 m top width and 10 m bank height, bed slope 0.05.
- **Friction**: Manning’s formulation with a global n of 0.05 s/m<sup>1/3</sup>.
- **Hydraulics**: steady inflow discharge of 1,558 m³/s applied at the right boundary (x = 450 m), free outflow on the left boundary (x = 0 m).
- **Initial state**: still water column 5 m deep with a small downstream velocity of 0.2 m/s to stabilise the solver before the boundary discharge ramps up.

## Tracer configuration
- One passive tracer is activated in `model.json` (`num_tracers = 1`) with zero initial concentration everywhere.
- A point source (`SOURCE` block) releases passive tracers at the rate of 500 m3/s from `point1`, (x $\approx$ 223 m, y $\approx$ m, mid-channel). 
- Outflow boundary on the left uses a zero-gradient condition for the tracer so mass can leave freely with the water.

## Numerical set-up
- Simulation time: 0–110 s with 5 s output interval. Requested fields: `flow_velocity`, `water_surface`, `tracer1` and its time derivative `tracer1_drv`.
- The mesh `trapezoidal_channel_mesh.2dm` has 4,474 nodes, 8,727 triangular cells and 13,200 edges. Region 2 is only used for the tracer source; hydraulics remain region-wise uniform.

## Input files:
- **model.json**: configuration file that specifies physical problem and some numerical settings, including the computational mesh .2dm file. BASEMENT **DOES NOT** directly use this file to run simulation but by default write its info into a setup.h5 file first, which was actually used later to execute simulation.
- **trapezoidal_channel_mesh.2dm**: unstructured triangular mesh file required by BASEHPC as computational domain. For definition of the .2dm file format please see [this web by SMS](https://www.xmswiki.com/wiki/SMS:2D_Mesh_Files_*.2dm?__cf_chl_tk=r_woYILHa12UMY664uxq5gFDzTZfQia_Lz7.6bShzj8-1759226996-1.0.1.1-1aZOLNVb_EeD1zsV.on53xi.Jr71gmBhP2pD1xdBYy0). This .2dm file used was initially generated using the script **trapezoidal_channel.py** from the [BASEmesh repo](https://gitlab.ethz.ch/vaw/public/basemesh-v2/-/tree/master/examples/basechange?ref_type=heads). It was later edited manually to add a few key lines needed for defining boundary and initial conditions according to the manual.
- **simulation.json**: configuration file that specifies:
  - Numerical settings controlling the computation process (e.g., time step).
  - What variables to store and the time interval for storing. 
    
    BASEMENT takes this file together with the setup.h5 file generated from **model.json** as input to launch the computation.
- **results.json**: configuration file that specifies converting the results.h5 file (generated during simulation) into a .xdmf file. Technically it's not right to say 'convert' since the .xdmf file does not really store any data and must always be used with results.h5 placing in the same folder.
- The .json configuration files were initially populated using the GUI provided. This is convenient to get started but not so much in the later fine tuning and debugging steps when you need come back and forth between some particular parameters and re-run the simulation. In the later case it's better to simply edit the .json file directly and call the BASEMENT executables in a terminal environment.

## Computation statistics
- Solver: BASEHPC OpenMP binary (BASEMENT v4.1.0) on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P).
- Runtime: 405.6 s CPU time for 110 s of simulated hydraulics and tracer transport.

## Post-processing
- Load `results.xdmf` in ParaView and apply the filters stored in `06_tracer.pvsm` to reproduce the GIF: water surface (blue-white ramp), velocity vectors, and a warm colour map for `tracer1`.
- The derivative field `tracer1_drv` is useful to spot when the source goes inactive and to quantify mixing length scales; the sample state file plots it alongside concentration isolines.
- Typical observations: the tracer cloud forms near x ≈ 225 m, hugs the thalweg because of higher velocities, and exits the domain between 60–80 s with little lateral diffusion—consistent with the negligible transverse velocity component in this steady, high-Reynolds channel flow.
![Animation_06](/06_tracer/ParaView/06_tracer.gif)