# Case 3: Malpasset dam break

## Physical settings:
- Domain geometry:
  - Real-world Malpasset dam break scenario (H_BP_4 test case)
  - Doubly-curved equal angle arch dam with variable radius
  - Storage lake upstream, dry bed downstream
  - Initial water surface elevation: +100.0 m.a.s.l. in lake, 0.0 m.a.s.l. downstream
  - Dam breach at t = 0, flood wave tracked for 300 seconds
- Flow scenario:
  - Sudden dam failure, rapid downstream flooding
  - Downstream area initially dry

## Numerical settings:
- Friction: Manning coefficient 0.033 
- Initial conditions:
  - Water surface elevation: 100.0 m (region 1), 0.0 m (region 2)
- Dynamic depth solver: on, precision 0.005
- Riemann solver: exact, tolerance 1e-06
- Minimum water depth: 0.05
- CFL number: 0.85

## Input files:
- **model.json**: configuration file specifying physical problem and numerical settings, including the computational mesh (.2dm file). BASEMENT writes its info into a setup.h5 file, which is used for simulation.
- **H_BP_4.2dm**: unstructured triangular mesh file required by BASEHPC as computational domain. For .2dm file format, see [SMS wiki](https://www.xmswiki.com/wiki/SMS:2D_Mesh_Files_*.2dm?__cf_chl_tk=r_woYILHa12UMY664uxq5gFDzTZfQia_Lz7.6bShzj8-1759226996-1.0.1.1-1aZOLNVb_EeD1zsV.on53xi.Jr71gmBhP2pD1xdBYy0). ![Meshing_03_malpassetdambreak](/03_malpassetdambreak/Physics/Meshing.jpg)
- **simulation.json**: configuration file specifying numerical settings, variables to store, and time intervals for storing. Used with setup.h5 to launch computation.
- **results.json**: configuration file for converting results.h5 to .xdmf for visualization. The .xdmf file references results.h5 and does not store data itself.

## Output files:
- **results.h5**: data output at timepoints specified in model.json or simulation.json
- **results.xdmf**: .xml file referencing results.h5 file so it can be read by ParaView. This file can be generated using BASEMENT GUI or BMv4_results.exe
- **.vtk files**: files storing data at all **nodes**, each  file stores data for one timepoint as specified in the SPECIAL_OUTPUT block in model.json 

## Computation statistics:
- Unstructured triangular mesh (22186 cells) solved on 16 CPU threads using BASEMD.
- CPU model: 12th Gen Intel(R) Core(TM) i7-1260P.
- cpu-time 21.544 s for 300 s physical time.

## Post-processing & visualization:
- The /QGIS folder stores project file for visualizing the .2dm mesh file
- The .psvd file in /ParaView stores the pipeline for loading, processing, and visualizing data (.xdmf and .h5 files). Open this file in ParaView after simulation.
- Animation of depth and velocity: ![Animation_03_malpassetdambreak](/03_malpassetdambreak/ParaView/03_malpassetdambreak.gif)