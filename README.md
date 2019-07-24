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
conda install overpass
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

You will see some geojson files creates in the data subdirectory which can use with umap.
