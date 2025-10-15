# Case 9: Restarting from Case 2 dambreak

## Physical settings
- Geometry and scenario are identical to Case 2 (flat 15 m × 1 m rectangular channel with an initial upstream reservoir and dry downstream). See [Case 2 README](/02_dambreak/README.md) for the schematic and details.
- This case demonstrates BASEMENT's restart capability by continuing the Case 2 dambreak solution from a saved state.

## Restart configuration
- Hydraulics initialisation uses `type = continue`, reading from a prior results file at a specified physical time:
  - Restart file: `results_old.h5` (produced by Case 2 and placed in this folder).
  - Restart time: 10.0 s (continues the solution from that saved step).
- Friction: Manning formulation (n = 0.6 s/m$^{1/3}$ as in `model.json`). This exceptionally high value was used to artificially accelerate the decaying of the dam break flood wave.

## Numerical settings
- Additional simulation window: 50 s beyond the restart point, with outputs every 0.2 s.
- Mesh: same unstructured triangular mesh as Case 2 with 231 cells and 154 nodes.

## Input files:
- **model.json**: restart configuration (`HYDRAULICS.INITIAL.type = continue`) with `file` pointing to `results_old.h5` and `time = 10.0` s; mesh and parameters as in Case 2.
- **two_region_basin.2dm**: unstructured triangular mesh used in Case 2 (231 triangles, 154 nodes).
- **simulation.json**: solver controls (time window, timestep control) and requested outputs (`water_depth`, `flow_velocity`).
- **results.json**: post-processing export to generate `results.xdmf` alongside `results.h5`.
- **results_old.h5**: this file stores multiple snapshots of the flow field, and the simulation may start from any of them. This can be obtained by coping the results file from Case 2 (e.g., `02_dambreak/results.h5` at 10 s) to this folder and rename to `results_old.h5`, or adjust `model.json` to the correct path.

## Computation statistics:
- Solver: BASEMENT (BASEHPC OpenMP build) on 16 CPU threads (12th Gen Intel(R) Core(TM) i7-1260P).
- Unstructured triangular mesh: 231 cells, 154 nodes.
- cpu-time = ____ s for the 50 s continuation.

## Post-processing & visualization:
- Load `results.xdmf` in ParaView and apply the saved state `09_restartsimulation/ParaView/09_restartsimulation.pvsm` to reproduce the visualisation.
- An example animation (3D view of water depth and water depth history at the monitoring point in the flume center) is provided here:
  ![Animation_09_restartsimulation](/09_restartsimulation/ParaView/09_restartsimulation.gif)
