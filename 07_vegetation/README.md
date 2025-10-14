# Case 7: Vegetation-bedload interaction in a widening channel

## Physical settings
- Geometry matches Case 4: a 50 m long channel that widens linearly from 20 m to 40 m with a bed slope of 0.01. The regenerated mesh (`widening_open_channel.2dm`) comprises 1,249 nodes and 2,380 triangular cells.
- Upstream discharge remains 20 m<sup>3</sup>/s. The domain starts dry, fills from the inflow boundary, and activates morphodynamics after 100 s.
- Bed material is a uniform gravel mixture with grain size 0.02 m, density 3,000 kg/m<sup>3</sup>, and porosity 0.4, identical to the reference case.

## Vegetation configuration
- A single vegetation region (`reg0`) covers the plane with initial non-dimensional above-ground biomass 0.3, below-ground biomass 0.5, and rooting depth 0.5 m.
- Vegetation parameters use BASEMENT's empirical closure: plant height scales with biomass (`plant_height_fact = 0.5`, `plant_height_exp = 0.2`), drag is amplified by `veg_strickler_fact = 0.1`, and the critical Shields stress for uprooting is scaled with `veg_theta_critical_fact = 0.9`. The parameters chosen **do not** necessarily reflect any real cases but were simply for demo purpose.
- Vegetation feedback is active from t = 0 s, so roughness, critical shear stress, and bedload thresholds respond to biomass changes once morphodynamics commence.

## Numerical settings
- Morphodynamics: Meyer-Peter and Mueller (1948) bedload transport formula, morphodynamic start at 100 s, sediment density 3,000 kg/m<sup>3</sup>, porosity 0.4.
- Simulation window: 0-500 s with 2 s write interval. Exported fields extend Case 4 by adding `aboveground_biomass` so vegetation evolution can be visualised alongside hydraulics and bed change.
- Solver: BASEMENT v4.1.0, BASEHPC OpenMP build. The fastest 16-thread run completed in roughly 3.3-3.7 s CPU time for the 500 s simulation.

## Input files
- `model.json` - Case 4 setup augmented with the `VEGETATION` block defining biomass fields, Strickler factor scaling, and critical shear adjustments.
- `widening_open_channel.2dm` - mesh generated via `widening_open_channel.py`, retaining the inflow/outflow string definitions consumed by hydraulics, morphology, and vegetation.
- `simulation.json` - solver control and output configuration, now including the biomass field.
- `results.json` - post-processing recipe that builds `results.xdmf` from `results.h5` for ParaView.
- `ParaView/07_vegetation.pvsm` - ParaView state used to generate `ParaView/07_vegetation.gif`, combining water surface, bed elevation change, velocity vectors, and the vegetation layer.

## Post-processing & visualization
- The ParaView state in `/07_vegetation/ParaView/07_vegetation.pvsm` restores the full pipeline (loading `results.xdmf`, applying contours/slices, and styling).
- An animation of water surface, bed elevation change, and vegetation cover is exported as `/07_vegetation/ParaView/07_vegetation.gif`.
![Animation_07](/07_vegetation/ParaView/07_vegetation.gif)
