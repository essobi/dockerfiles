## Emacs, make this -*- mode: sh; -*-  
## start with the Docker 'R-devel' Debian-based image  
FROM rocker/drd:latest  
  
## maintainer of this script  
MAINTAINER Alex Chubaty <alex.chubaty@gmail.com>  
  
## 1. Remain current;  
## 2. Add additional build dependencies for R spatial packages;  
## 3. Install `recommended` so Rdevel can use them  
## (Rdevel was installed using `--without-recommended`,  
## so it doesn't 'see' these packages during `R CMD check`);  
## 4. Install devtools;  
## 5. Install R spatial packages;  
## 6. Cleanup downloaded packages.  
##  
## All of this is run in a single RUN command to get a single AUFS layer  
RUN apt-get update -qq \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y --no-install-recommends -t unstable \  
bwidget \  
curl \  
gdal-bin \  
git \  
gsl-bin \  
libcurl4-openssl-dev \  
libgdal-dev \  
libgeos-dev \  
libgeos++-dev \  
libreadline-dev \  
libproj-dev \  
libspatialite-dev \  
libssl-dev \  
libudunits2-dev \  
libv8-dev \  
libxml2-dev \  
netcdf-bin \  
pandoc pandoc-citeproc\  
qpdf \  
r-cran-rgl \  
r-cran-tkrplot \  
&& RDscript -e 'recommended <\-
unname(installed.packages(priority="recommended")[,"Package"]);
install.packages(recommended, lib=.Library, dependencies=TRUE)' \  
&& install.r devtools remotes \  
&& xvfb-run -a install.r \  
geoR \  
ggmap \  
ggvis \  
gstat \  
mapdata \  
maps \  
maptools \  
plotKML \  
RandomFields \  
rgdal \  
rgeos \  
sf \  
shapefiles \  
sp \  
spatstat \  
raster \  
rasterVis \  
rts \  
&& installGithub.r s-u/fastshp \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& apt-get autoremove -qy \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/apt/lists  

