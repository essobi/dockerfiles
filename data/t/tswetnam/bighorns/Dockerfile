FROM rocker/verse:latest  
MAINTAINER "Tyson Swetnam" tswetnam@cyverse.org  
  
# Original Dockerfile from Rocker/Geospatial  
# Added several additional R packages and dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
lbzip2 \  
libfftw3-dev \  
libgdal-dev \  
libgeos-dev \  
libgsl0-dev \  
libgl1-mesa-dev \  
libglu1-mesa-dev \  
libhdf4-alt-dev \  
libhdf5-dev \  
libjq-dev \  
liblwgeom-dev \  
libproj-dev \  
libprotobuf-dev \  
libnetcdf-dev \  
libsqlite3-dev \  
libssl-dev \  
libudunits2-dev \  
netcdf-bin \  
protobuf-compiler \  
tk-dev \  
unixodbc-dev \  
&& install2.r --error \  
RColorBrewer \  
RandomFields \  
RNetCDF \  
classInt \  
deldir \  
gstat \  
hdf5r \  
lidR \  
mapdata \  
maptools \  
mapview \  
ncdf4 \  
proj4 \  
raster \  
rgdal \  
rgeos \  
rlas \  
sf \  
sp \  
spacetime \  
spatstat \  
spdep \  
geoR \  
geosphere \  
# Added Packages  
PerformanceAnalytics \  
boot \  
devtools \  
dlm \  
dplyr \  
foreign \  
lubridate \  
plotly \  
truncreg \  
## from bioconductor  
&& R -e "BiocInstaller::biocLite('rhdf5')"  

