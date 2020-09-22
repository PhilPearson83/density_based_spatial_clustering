import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os.path as path
from sklearn.cluster import DBSCAN
from sklearn import metrics
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
import pyodbc
from pyproj import Proj, transform

# find working folder
dir_path = path.dirname(path.realpath(__file__))

# connection to server and databse
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=SQL1\\LIVE1;"
    "Database=CommonData;"
    "Trusted_Connection=yes;"
)
# Read the sql file
query = open(dir_path + "/" + "ers_failures.sql", "r")
# read the sql query and connection and create a dataframe
df = pd.read_sql(query.read(), conn)
# convert x/y columns to number from text
df["EASTING"] = df["EASTING"].apply(lambda x: int(x))
df["NORTHING"] = df["NORTHING"].apply(lambda x: int(x))
# df[["EASTING", "NORTHING"]] = df[["EASTING", "NORTHING"]].apply(pd.to_numeric)
print(df.info())

v84 = Proj(proj="latlong", towgs84="0,0,0", ellps="WGS84")
v36 = Proj(
    proj="latlong",
    k=0.9996012717,
    ellps="airy",
    towgs84="446.448,-125.157,542.060,0.1502,0.2470,0.8421,-20.4894",
)
vgrid = Proj(init="world:bng")


def dfENtoLL84(df):
    vlon36, vlat36 = vgrid(df["EASTING"].values, df["NORTHING"].values, inverse=True)
    result = transform(v36, v84, vlon36, vlat36)
    # Transform the output to a Dataframe
    latlong = pd.DataFrame(index=df.index)
    for i in result:
        latlong["lon"] = result[0]
        latlong["lat"] = result[1]
    return latlong


def vectorized_convert(df):
    vlon36, vlat36 = vgrid(df["EASTING"].values, df["NORTHING"].values, inverse=True)
    converted = transform(v36, v84, vlon36, vlat36)
    df["lat"] = converted[0]
    df["lon"] = converted[1]
    return df


df2 = pd.DataFrame({"NORTHING": [378778, 384732], "EASTING": [366746, 364758]})
vec = vectorized_convert(df)
# print(vec)
# vec.to_csv("dd.csv", index=False)


coords = vec[["lat", "lon"]].values

kms_per_radian = 6371.0088
epsilon = 4 / kms_per_radian
db = DBSCAN(eps=epsilon, min_samples=10, metric="haversine", algorithm="ball_tree").fit(
    np.radians(coords)
)
cluster_labels = db.labels_
print(cluster_labels)
# calculate the number of clusters
num_clusters = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)
print("Number of clusters: {}".format(num_clusters))

clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
print(clusters)
# identify core points
core_points = np.zeros_like(cluster_labels, dtype=bool)
core_points[db.core_sample_indices_] = True
# print(core_points)
print(
    "Silhouette Coefficient: %0.3f" % metrics.silhouette_score(coords, cluster_labels)
)


def get_centermost_point(cluster):
    centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
    centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
    return tuple(centermost_point)


centermost_points = clusters.map(get_centermost_point)
# print(centermost_points)
#centermost_points.to_csv("centre.csv", index=False)
lats, lons = zip(*centermost_points)
rep_points = pd.DataFrame({"lat": lats, "lon": lons})
rs = rep_points
# rs = rep_points.apply(lambda row: df[(df['lat']==row['lat']) &amp;&amp; (df['lon']==row['lon'])].iloc[0], axis=1)

fig, ax = plt.subplots(figsize=[10, 6])
rs_scatter = ax.scatter(
    rs["lat"], rs["lon"], c="#99cc99", edgecolor="None", alpha=0.7, s=200
)
df_scatter = ax.scatter(df["lat"], df["lon"], c="k", alpha=0.9, s=3)
ax.set_title("Full data set vs DBSCAN reduced set")
ax.set_xlabel("Latitude")
ax.set_ylabel("Longitude")
ax.legend([df_scatter, rs_scatter], ["Full set", "Reduced set"], loc="upper right")
plt.show()
