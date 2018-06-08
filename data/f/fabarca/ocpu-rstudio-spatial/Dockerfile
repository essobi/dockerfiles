FROM opencpu/rstudio  
  
  
RUN add-apt-repository -y ppa:ubuntugis/ppa && \  
add-apt-repository -y ppa:opencpu/jq && \  
apt-get update && \  
apt-get install -y \  
libjq-dev \  
wget \  
lbzip2 \  
libcairo2-dev \  
libdap-dev \  
libexpat1-dev \  
libfftw3-dev \  
libfreexl-dev \  
libgdal-dev \  
libgeos-dev \  
libgsl0-dev \  
libglu1-mesa-dev \  
libhdf4-alt-dev \  
libhdf5-dev \  
liblwgeom-dev \  
libkml-dev \  
libnetcdf-dev \  
libproj-dev \  
libsqlite3-dev \  
libssl-dev \  
libtcl8.5 \  
libtk8.5 \  
libtiff5-dev \  
libudunits2-dev \  
libv8-dev \  
libxerces-c-dev \  
netcdf-bin \  
gdal-bin \  
protobuf-compiler \  
unixodbc-dev \  
python-pip \  
python-virtualenv  
  
  
# Install wgrib2 binary  
# Ref:
http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/compile_questions.html  
  
RUN cd /tmp && \  
wget ftp://ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/wgrib2.tgz && \  
tar -xzvf wgrib2.tgz && \  
cd /tmp/grib2 && \  
export CC=gcc && \  
export FC=gfortran && \  
make && \  
cp wgrib2/wgrib2 /usr/local/bin/wgrib2 && \  
cd .. && \  
rm -r grib2 wgrib2.tgz  
  
  
  
  
## Install R packages  
  
RUN Rscript -e "install.packages(c( \  
'automap', \  
'deldir', \  
'DCluster', \  
'classInt', \  
'fastcluster', \  
'gdalUtils', \  
'geojsonio', \  
'geoR', \  
'geosphere', \  
'gstat', \  
'igraph', \  
'lidR', \  
'leaflet', \  
'maptools', \  
'ncdf4', \  
'proj4', \  
'postGIStools', \  
'plotly', \  
'rasterVis', \  
'raster', \  
'rgdal', \  
'rgeos', \  
'rlas', \  
'rmapshaper', \  
'roxygen2', \  
'RandomFields', \  
'RColorBrewer', \  
'RSQLite', \  
'RMySQL', \  
'sf', \  
'sp', \  
'spacetime', \  
'spatstat', \  
'spdep', \  
'splancs', \  
'testthat', \  
'devtools', \  
'usethis', \  
'checkmate', \  
'dplyr', \  
'tidyverse', \  
'future', \  
'nnet', \  
'keras', \  
'caret' \  
), repos='https://cloud.r-project.org/'); \  
source('https://bioconductor.org/biocLite.R'); \  
biocLite('BiocInstaller'); \  
BiocInstaller::biocLite('rhdf5')"  
  
RUN mkdir /opt/virtualenvs && \  
chmod +rx /opt/virtualenvs && \  
echo "WORKON_HOME=\"/opt/virtualenvs\"" >> /etc/R/Renviron  
  
  
RUN Rscript -e "library(keras); install_keras()"  
  

