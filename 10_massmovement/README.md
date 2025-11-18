# Case 10: Wave generation by sudden bottom downthrow (mass movement)

## Physical settings
The settings for this simulation were covered in the series of flume experiment by  Hammack (1973) (see the paper in `10_massmovement/Ref`)
- Geometry: long, rectangular flume `10000 m × 50 m` with constant still-water depth `h = 10 m`.
- Regions: the bed is split into a central movable strip and two fixed flanks by two vertical lines at `x = ±b` with `b = 122 m` (measured from the flume centre). The central strip is tagged as `movable`, the outer strips as `fixed`.
- Scenario: a sudden downthrow of the movable bottom generates a surface-gravity wave that propagates away from the source, following the laboratory configuration described in the reference paper in `10_massmovement/Ref`.
![Schematic](/10_massmovement/Physics/Schematic.jpg)

## Numerical settings
- Unstructured triangular mesh: 51,861 cells, 27,919 nodes.
- Time window: `0–540 s`, output interval `1 s`.
- Timestep control: initial `0.02 s`, minimum `1e-4 s`, CFL limit `0.9`; minimum water depth `0.01 m`.
- Mesh: unstructured triangular mesh with `51,861` cells and `27,919` nodes.

## Input files:
- **model.json**: defines geometry (`massmovement.2dm`), region names (`fixed`, `movable`), hydraulics at rest, and the `MASSMOVEMENT` block (thickness = 1 m over `movable`). BASEMENT **DOES NOT** directly use this file to run simulation but by default write its info into a setup.h5 file first, which was actually used later to execute simulation.
- **massmovement.2dm**: unstructured triangular mesh file required by BASEHPC as computational domain. For definition of the .2dm file format please see [this web by SMS](https://www.xmswiki.com/wiki/SMS:2D_Mesh_Files_*.2dm?__cf_chl_tk=r_woYILHa12UMY664uxq5gFDzTZfQia_Lz7.6bShzj8-1759226996-1.0.1.1-1aZOLNVb_EeD1zsV.on53xi.Jr71gmBhP2pD1xdBYy0). The .2dm file used here was generated using the script.
- **massmovement.py** adapted from the usage_example.py at [BASEmesh repo](https://gitlab.ethz.ch/vaw/public/basemesh-v2/-/tree/master/examples/basechange?ref_type=heads). 
- **simulation.json**: solver controls (time window, time step) and requested outputs: `water_surface`, `bottom_elevation`, `delta_z`.
    BASEMENT takes this file together with the setup.h5 file generated from **model.json** as input to launch the computation.
- **results.json**: configuration file that specifies converting the results.h5 file (generated during simulation) into a .xdmf file. Technically it's not right to say 'convert' since the .xdmf file does not really store any data and must always be used with results.h5 placing in the same folder.

## Computation statistics:
- Solver: BASEMENT (BASEHPC OpenMP build) on 10 CPU threads (CPU model: Inter Core Ultra 9 285).
- cpu-time = `3.13 s` for 540 s physical time.

## Post-processing & visualization:
- ParaView: load `results.xdmf` and apply the saved state `10_massmovement/ParaView/10_massmovement.pvsm` to reproduce probe sampling and views. CSV time series at four probe locations (`p1.csv`–`p4.csv`) are saved from ParaView to `10_massmovement/ParaView/`.
- MATLAB plotting: change into the directory `10_massmovement/Figures` and run `Figures/mkplot_massmovement.m` to plot model vs. experiment at probes P1–P4 using `Ref/experiment.mat`. The script exports `Figures/model_experiment_comparison.png` as below ($\eta$ = surface elevation, i.e. vertical displacement of free surface from still water surface).
![Plot_10_massmovement](/10_massmovement/Figures/model_experiment_comparison.png)