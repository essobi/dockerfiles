# Dockerfiles

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1287013.svg)](https://doi.org/10.5281/zenodo.1287013)

This is the dockerfiles [Dinosaur Dataset](https://vsoch.github.io/datasets)

![https://vsoch.github.io/datasets/assets/img/avocado.png](https://vsoch.github.io/datasets/assets/img/avocado.png)

## Generation

 1. The set of words from [search-terms.json](search-terms.json) is read and parsed for prefixes. The prefixes are used to search for Docker containers (using the docker command line tool with limit 100) so find unique images that match. We do this search and save the results to pickle files until all terms are used. This happens in the script [0.find_containers.py](0.find_containers.py).
 2. Once we have many pickle files, each with a list of containers, we use [1.download_dockerfiles.py](1.download_dockerfiles.py) to issue web requests to do the downloads. The data is stored under [data](data) in lettered folders based on the first letter of the username, and then subfolders with username and reponame, respectively.
