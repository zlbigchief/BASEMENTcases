# BASEMENTcases

This project will be my self-tutorial courses for learning how to use [BASEMENT v4.1](https://basement.ethz.ch/download/software-download.html) and postprocessing results in ParaView or QGIS. I try to set up, run and postprocessing a few cases. Each case will be stored with its own scripts for pre- and post-processing and input files.

## About BASEMENT:
The software system BASEMENT(BAsic-Simulation-EnvironMENT) is a software developed at VAW of ETH Zurich for simulating river flow, sediment transport and other material transports, harnessing the parallel computation of CPU/GPU hybrid architecture. The software provides a functional environment for numerical simulation of river flows with sediment transport in alpine and sub-alpine regions. The main focus of conception and development is the robustness of the numerical models, the flexibility of the computational grid and the combination and efficiency of the method of calculation (problem dependent equations, coupling of models, parallelization).

There are a few PDF manuals and documents coming together with the software after installation:
- **Intro and installation**: how to install BASEMENT for Windows and Linux systems and release notes of latest features and changes in recent versions
- **User manual**: describing the modelling environment of BASEMENT (particularly the super user-friendly GUI), including the three stages of pre-processing, simulation and postprocessing.
- **Reference manual BASEMD**: information about the mathematical models and numerical approximations in BASEMD module
- **Reference manual BASEHPC**: information about the mathematical models and numerical approximations in BASEHPC module
- **Tutorials**: Guidance on how to use BASEmesh and how to postprocessing results using QGIS and ParaView; Step-by-step guides on how to set up realistic cases
- **Testcases**: collection of common benchmark cases for testing hydrodynamic, sediment and vegetation modules; domain coupling and high-performance computation.

Those files can be found from in the /share/doc folder in the installation path.

## Simulation cases and file structure
Below are introductions of the physical settings, computational stats and quick views of the results. For detailed documentations of each case please see the README.md in each case folder.

### Case 1: Open channel flow

[More details in the case README](./01_openchannelflow/README.md)

The physical settings for this case include a trapezoidal channel geometry with a bottom width of 20 m, top width of 60 m, and height of 10 m, extending horizontally for 450 m with a bed slope of 0.05 and a Manning friction coefficient of 0.05 s/m<sup>1/3</sup>. The flow parameters feature an incoming discharge of 1558 m<sup>3</sup>/s. 

Computation statistics are based on an unstructured triangular mesh of 8,727 cells, solved using BASEHPC on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P), with a total CPU time of 256.512 seconds for 110 seconds of simulated physical time. For comparison, the total CPU time is 505.452 seconds when using 2 CPU threads.

The water depth and velocity vector field form t = 0 to 110 s looks like 
![Animation_01](/01_openchannelflow/ParaView/01_openchannelflow.gif)

### Case 2: Dam break

[More details in the case README](./02_dambreak/README.md)

This case simulates the sudden failure of a dam, resulting in rapid downstream flooding. The domain consists of a flat rectangular channel 15 m long and 1 m wide, with an initial water level of 10 m upstream of the dam and a dry bed downstream. ![Schematic_02](/02_dambreak/Physics/Schematic.jpg) Both the up- and downstream boundaries are treated as vertical walls.

The computational mesh uses 231 unstructured triangular cells (see below). ![Meshing_02](/02_dambreak/Physics/meshing.jpg) The simulation is performed with BASEHPC on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P), requiring only 0.075 seconds of CPU time for 10 seconds of simulated physical time. 

The simulated water surface and velocity look like:
![Animation_02](/02_dambreak/ParaView/02_dambreak.gif)

### Case 3: Malpasset dam break

[More details in the case README](./03_malpassetdambreak/README.md)

This case reproduces the H_BP_4 case documented in the Testcases.pdf shipped with BASEMENT. This hydraulic test case benefits from the well known real world dataset from the Malpasset dam break in France. The complex geometry, high velocities, often and sudden wet-dry changes and the good documentation allow for a fundamental evaluation of the hydraulic code.

The Malpasset dam was a doubly-curved equal angle arch type with variable radius. It breached on December 2nd, 1959 all of a sudden. The entire wall collapsed nearly completely what makes this event unique. The breach created a water flood wall 40 meters high and moving at 70 km/h. After 20 minutes, the flood reached the village Frejus and still had 3 m depth. The time of the breach and the flood wave can be exactly reconstructed, as the time is known, when the power of different stations switched off.

The figure below shows the computational grid used for the simulation, which can be downloaded from [here](https://people.ee.ethz.ch/~basement/baseweb/download/testcases/BASEMD/hydr-TC-2D/H-BP-4.zip). ![Meshing_03](/03_malpassetdambreak/Physics/Meshing.jpg) The initial water surface elevation in the storage lake is set to +100.0 m.a.s.l. and in the downstream lake to 0.0 m.a.s.l. The area downstream of the wall is initially dry. At t=0, the dam is removed and we track the flood wave up to 300 seconds. For detailed description please see the README in the /03_malpassetdambreak or section 1.4.4 H_BP_4: Malpasset dam break in the [Testcases](https://people.ee.ethz.ch/~basement/baseweb/download/documentation/BMdoc_Testcases_v4-1-0.pdf) document.

The 22186 cells were solved on 16 CPU threads using BASEMD module. The cpu-time is 21.544 s for 300 s physical time (CPU model: CPU model: 12th Gen Intel(R) Core(TM) i7-1260P).
The following animation was generated using ParaView to open the .vtk format outputs, this can be done by setting the format to be 'vtk' in the SPECIAL_OUTPUT block in model.json file
![Animation_03](/03_malpassetdambreak/ParaView/03_malpassetdambreak.gif)

```
"OUTPUT": {
  "SPECIAL_OUTPUT": [
    {
      "format": "vtk",
      ...
    }
  ]
}
```
 
Alternatively, animation in QGIS by changing the format to shape is also possible but needs a bit more post-processing by the user (see this [README](/03_malpassetdambreak/README.md) for details.)

### Case 4: Bed load transport

[More details in the case README](./04_bedloadtransport/README.md)

This case tests the bed load transport and morphological modules in BASEHPC. The senario of stationary flow in a widening open channel is simulated. It is expected that as the channel widens and the flow decelerates, the bed load transport decreases downstream and thus the bed elevates due to accretion. 

Specifically, the channel increases from 20 m wide at the upstream inflow boundary to be 40 m wide at the outflow boundary 50 m downstream. ![Schematic_04](/04_bedloadtransport/Physics/Schematic.jpg) The model was initialised with 20 m<sup>3</sup>/s discharge and a dry bed, which was set to be fixed bed in the first 100 seconds. After that the bed load transport module was activated and accordingly the morphological change was simulated. A uniform bed of grain size 0.02 m, density 3000 kg/m<sup>3</sup> and porosity 0.4 was adopted. The bed load transport was computed using the Meyer-Peter and Müller (1948) model (see MPM model in the reference manuals for details of the mathematical model implemented in the sediment transport module of BASEMENT).

The computational mesh uses 2380 unstructured triangular cells ![Meshing_04](/04_bedloadtransport/Physics/Meshing.jpg) The simulation is performed with BASEHPC on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P), requiring 3.13 seconds of CPU time for 500 seconds of simulated physical time. 

Shown below are the 3D view of water surface and bed elevation ![Animation_04_3D](/04_bedloadtransport/ParaView/04_bedloadtransport_3Dview.gif) as well as the 2D profile along the channel central line. ![Animation_04_2D](/04_bedloadtransport/ParaView/04_bedloadtransport_2Dview.gif)

### Case 5: Suspended sediment transport

[More details in the case README](./05_suspendedsedimenttransport/README.md)

This case demonstrates suspended sediment transport and morphological change in a widening open channel using BASEHPC. The computational domain and mesh are the same as in Case 4, but the focus is on sediment picked up by water flow rather than bed load transport.

Sediment properties include a grain size of 0.005 m (5 mm), sediment density of 2650 kg/m³, porosity of 0.4, and a critical Shields parameter of 0.02. The bedload transport module is formally included but its pre-factor is set to zero, so morphological change is solely induced by suspended sediment erosion.

The computational mesh consists of 2380 unstructured triangular cells (same as Case 4), solved on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P) with a cpu-time of 3.13 seconds for 400 seconds of physical time simulation.

Post-processing and visualization are performed in ParaView using the .psvd file in /ParaView. Visualizations include water surface elevation, suspended sediment concentration, and bed elevation changes. ![Animation_05](/05_suspendedsedimenttransport/ParaView/05_suspendedsedimenttransport.gif)

### Case 6: Passive tracer transport

[More details in the case README](./06_tracer/README.md)

This scenario reuses the trapezoidal channel of [Case 1](#case-1-open-channel-flow) but activates BASEHPC's tracer module to release a passive dye pulse into the 1,558 m<sup>3</sup>/s steady inflow. A single point source inside the mesh emits the tracer mass while a zero-gradient outlet lets it flush out of the domain.

The simulation runs for 110 s on the 8,727-cell mesh, saving velocity, water surface, tracer concentration, and its time derivative every 5 s. ParaView assets in `/06_tracer/ParaView` reproduce the plume evolution. ![Animation_06](/06_tracer/ParaView/06_tracer.gif)

### Case 7: Vegetation-bedload interaction

[More details in the case README](./07_vegetation/README.md)

Case 7 extends the widening channel of [Case 4](#case-4-bed-load-transport) by enabling BASEMENT's vegetation feedbacks. Uniform discharge of 20 m<sup>3</sup>/s enters a 50 m reach where initial biomass alters hydraulic roughness and critical Shields stress before morphodynamics activate after 100 s.

Outputs include water depth, bed change, velocity, and above-ground biomass every 2 s over 500 s of simulated time, allowing comparison between vegetated and bare-bed responses. ParaView visualisations in `/07_vegetation/ParaView` combine morphology and vegetation layers. ![Animation_07](/07_vegetation/ParaView/07_vegetation.gif)

### Case 8: Sunlit heating in a still-water pool

[More details in the case README](./08_temperature/README.md)

This case demonstrates the temperature module in a quiescent pool exposed to sunlight. The domain is a short trapezoidal channel with a central widening forming a pool region where a meteorological heat source (air 20 °C, RH 80%, wind 5 m/s, no shade, 400 W/m² radiation) acts only over the pool. Temperature diffuses with constant longitudinal/transverse coefficients of 0.2 m²/s. The run covers 0–3600 s with 20 s output interval on an unstructured triangular mesh of 3,374 cells and 1,761 nodes.

Mesh preview and animation:
![Meshing_08](/08_temperature/QGIS/Meshing.jpg)
![Animation_08](/08_temperature/ParaView/08_temperature.gif)

### Case 9: Restart simulation from Case 2

[More details in the case README](./09_restartsimulation/README.md)

This case showcases BASEMENT's restart capability by continuing the dambreak simulation of Case 2 from a saved state at t = 10 s (`results_old.h5`). It uses the same two-region rectangular channel mesh as Case 2 (231 triangles, 154 nodes) and advances for an additional 50 s with outputs every 0.2 s.

Animation of the continued run:
![Animation_09](/09_restartsimulation/ParaView/09_restartsimulation.gif)
