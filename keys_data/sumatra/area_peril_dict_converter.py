from shapely.geometry import Point
import geopandas as gpd
import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "areaperil_dict.csv"))
df.rename(columns={column:column.lower() for column in df.columns}, inplace=True)

# create the GeoDataFrame and its geometry
gdf_peril_area = gpd.GeoDataFrame(df)
gdf_peril_area["geometry"] = gdf_peril_area.apply(lambda row: Point([(row["lon"], row["lat"])]), axis=1)

# store to parquet format
gdf_peril_area.to_parquet(os.path.join(os.path.dirname(__file__), "areaperil_dict.parquet"))

