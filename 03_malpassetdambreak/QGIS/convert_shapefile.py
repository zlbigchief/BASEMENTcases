import geopandas as gpd
import pandas as pd
from pathlib import Path

# === Input shapefile ===
shp = Path("H_BP_4_nds_depth.shp")  # adjust path if needed

# === Read shapefile ===
gdf = gpd.read_file(shp)

# Identify the time fields (numeric names like '0', '10', '20'...)
time_fields = [c for c in gdf.columns if c.replace('.', '', 1).isdigit()]

# Convert from wide to long format
df_long = gdf.melt(
    id_vars=[c for c in gdf.columns if c not in time_fields],
    value_vars=time_fields,
    var_name="time",
    value_name="depth"
)

# Convert time strings to numeric (if possible)
df_long["time"] = pd.to_numeric(df_long["time"], errors="ignore")

# Make it a GeoDataFrame again
gdf_long = gpd.GeoDataFrame(df_long, geometry="geometry", crs=gdf.crs)

# === Save output ===
out = Path("H_BP_4_nds_depth_long.gpkg")
gdf_long.to_file(out, driver="GPKG")

print(f"✅ Saved time-expanded file to: {out}")
