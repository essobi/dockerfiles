# Dockerfiles

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1287013.svg)](https://doi.org/10.5281/zenodo.1287013)

This is the dockerfiles [Dinosaur Dataset](https://vsoch.github.io/datasets)


<a target="_blank" href="https://camo.githubusercontent.com/d0eb19f161d4795a9c137b9b71c70b008d7c5e8e/68747470733a2f2f76736f63682e6769746875622e696f2f64617461736574732f6173736574732f696d672f61766f6361646f2e706e67"><img src="https://camo.githubusercontent.com/d0eb19f161d4795a9c137b9b71c70b008d7c5e8e/68747470733a2f2f76736f63682e6769746875622e696f2f64617461736574732f6173736574732f696d672f61766f6361646f2e706e67" alt="https://vsoch.github.io/datasets/assets/img/avocado.png" data-canonical-src="https://vsoch.github.io/datasets/assets/img/avocado.png" style="max-width:100%; float:right" width="100px"></a>


## Generation

 1. The set of words from [search-terms.json](search-terms.json) is read and parsed for prefixes. The prefixes are used to search for Docker containers (using the docker command line tool with limit 100) so find unique images that match. We do this search and save the results to pickle files until all terms are used. This happens in the script [0.find_containers.py](0.find_containers.py).
 2. Once we have many pickle files, each with a list of containers, we use [1.download_dockerfiles.py](1.download_dockerfiles.py) to issue web requests to do the downloads. The data is stored under [data](data) in lettered folders based on the first letter of the username, and then subfolders with username and reponame, respectively.
