# Density Based Clustering of Applications with Noise (DBSCAN)

This repository contains example code and documentation for clustering data using dbscan algorithm and displaying the resultant output on a map generated using Folium.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PhilPearson83/density_based_spatial_clustering/HEAD?filepath=spatial_clustering.ipynb)

This repository contains example code and documentation for clustering data using dbscan algorithm and displaying the resultant output on a map generated using Folium.

<p align="center">
<a href="https://github.com/andy-landy/traceback_with_variables/actions"><img alt="Actions Status" src="https://github.com/andy-landy/traceback_with_variables/workflows/Tests/badge.svg"></a>
<a href="https://codecov.io/gh/andy-landy/traceback_with_variables"><img alt="Codecov" src="https://codecov.io/gh/andy-landy/traceback_with_variables/branch/master/graph/badge.svg"></a>
<a href="https://lgtm.com/projects/g/andy-landy/traceback_with_variables/context:python"><img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/andy-landy/traceback_with_variables.svg"/></a>
<a href="https://github.com/andy-landy/traceback_with_variables/blob/master/LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/andy-landy/traceback_with_variables?color=informational"></a>
<a href="https://pypi.org/project/traceback_with_variables/"><img alt="PyPI" src="https://img.shields.io/pypi/v/traceback_with_variables"></a>
<a href="https://anaconda.org/conda-forge/traceback-with-variables"><img src="https://img.shields.io/conda/vn/conda-forge/traceback-with-variables"></a>
<a href="https://pypi.org/project/traceback_with_variables/"><img alt="PyPI" src="https://img.shields.io/badge/python-3.5+-blue.svg"></a>
<a href="https://superuser.com/questions/413073/windows-console-with-ansi-colors-handling"><img title="windows, mac, linux etc." alt="Platform" src="https://img.shields.io/badge/platform-all-blue.svg"></a>
<a href="https://github.com/andy-landy/traceback_with_variables/blob/master/traceback_with_variables/override.py#L9"><img title="type hints everywhere" alt="Annotations coverage" src="https://img.shields.io/badge/type--hints-100%25-blueviolet.svg"></a>
<a href="https://github.com/andy-landy/traceback_with_variables/blob/master/traceback_with_variables/override.py#L8"><img title="no obscure objects, only transparent functions and data classes" alt="No-OOP" src="https://img.shields.io/badge/no OOP-100%25-blueviolet.svg"></a>
<a href="https://github.com/andy-landy/traceback_with_variables/blob/master/setup.py"><img alt="Dependencies" src="https://img.shields.io/badge/dependencies-0-blueviolet.svg"></a>
<a href="https://gitter.im/andy-landy/traceback-with-variables"><img alt="Gitter" src="https://img.shields.io/gitter/room/andy-landy/traceback-with-variables?color=blueviolet"></a>
<!--
<a href="https://pepy.tech/project/traceback_with_variables"><img alt="pip Downloads" src="https://static.pepy.tech/personalized-badge/traceback-with-variables?period=total&units=none&left_color=grey&right_color=orange&left_text=pip downloads"></a>
<a href="https://anaconda.org/conda-forge/traceback_with_variables/"><img alt="conda-forge Downloads" src="https://img.shields.io/conda/dn/conda-forge/traceback-with-variables?color=orange&label=conda%20downloads"></a>
-->
</p>


![us](./example/example.png)

# Directory Layout

```
.
├── data
│   ├── geospatial
│   │   ├── DSFRS_Service_Area.cpg
│   │   ├── DSFRS_Service_Area.dbf
│   │   ├── DSFRS_Service_Area.prj
│   │   ├── DSFRS_Service_Area.qpj
│   │   ├── DSFRS_Service_Area.shp
│   │   └── DSFRS_Service_Area.shx
│   └── dsfrs_stations.csv
├── example
│   ├── example.png
│   └── example_data.csv
├── .gitignore
├── Licence
├── README.md
├── ers_failures.sql
├── requirements.txt
└── spatial_clustering.ipynb
```
## Getting Started.

### Installation
First clone the repository and navigate to the project's root directory:
```bash
git clone https://github.com/PhilPearson83/density_based_spatial_clustering.git
cd density_based_spatial_clustering
```

This project is written in [`Python`](https://www.python.org/) and depends on the packages in the requirements.txt.

You can install these packages by running the following command in the project's root directory:

```bash
# pip install requirements.txt 
```
