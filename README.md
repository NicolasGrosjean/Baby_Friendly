# Baby Friendly
> Tool to maintain the [Grenoble Baby Friendly map](http://umap.openstreetmap.fr/fr/map/grenoble-baby-friendly_348445)

## Installation

Download or clone this repository.

### Python
I recommend you to install a Python environment with conda or virtualenv.

For example with conda, 
[download and install miniconda](https://docs.conda.io/en/latest/miniconda.html)

Create a conda environment
```
conda create -n baby_friendly python=3.7
```

Activate the conda environment
```
activate baby_friendly
```

Install the packages with the following commands
```
conda install geojson requests
```

## Usage

Activate the conda environment
```
activate baby_friendly
```

Run the script

```
python database.py
```

You will see some geojson files creates in the data subdirectory which can be used with umap.

## Stats

In Grenoble sector (45.1416, 5.6732, 45.2270, 5.7826), the geojson contains data about :

|Date      |Diaper|Highchair|Microwave|Toys|Calm|Stroller parking|Kindergarten|Playground|
|----------|------|---------|---------|----|----|----------------|------------|----------|
|2019-09-04|19    |10       |10       |7   |7   |10              |41          |282       |
|2019-08-03|19    |9        |10       |7   |7   |10              |40          |275       |

## Licence

The project have an Apache-2.0 licence because of the inclusion of
[overpass](https://github.com/mvexel/overpass-api-python-wrapper) which has this licence.