FROM rocker/geospatial:3.3.3  
MAINTAINER Kyle Bocinsky <bocinsky@gmail.com>  
  
RUN apt-get update  
  
## ffmpeg  
RUN apt-get install -y --no-install-recommends \  
git \  
libx264-dev \  
yasm \  
&& git clone \--depth 1 git://source.ffmpeg.org/ffmpeg \  
&& cd ffmpeg \  
&& ./configure --enable-gpl --enable-libx264 \  
&& make -j4 \  
&& make install \  
&& cd .. \  
rm -rf ffmpeg  
  
## ghostscript, pandoc, and citeproc  
RUN apt-get install -y --no-install-recommends \  
ghostscript  
  
## Update currently installed R packages to MRAN version  
RUN r -e
'update.packages(repos="https://mran.microsoft.com/snapshot/2017-05-15",
ask=FALSE)'  
  
## Install R package dependencies from stable MRAN repo  
RUN install2.r -r 'https://mran.microsoft.com/snapshot/2017-05-15' \--error \  
## Packages for Python-like command-line parsing  
devtools \  
optparse \  
## Package for data aquisition  
FedData \  
## Packages for parallel processing  
foreach \  
doParallel \  
## Packages offering general utilities  
R.utils \  
Hmisc \  
zoo \  
abind \  
mgcv \  
rgbif \  
fields \  
## Packages for spatial processing  
sf \  
rgdal \  
ncdf4 \  
raster \  
geomapdata \  
maptools \  
mapproj \  
## Packages for chronometric analysis  
Bchron \  
mclust \  
## Packages for tidy code  
magrittr \  
tidyverse \  
ggthemes \  
purrrlyr \  
## Plotting  
RColorBrewer \  
htmlwidgets \  
plotly \  
bibtex \  
knitcitations  
  
## Update ggplot2 to development version (need 2.2.1.9000 for geom_sf
function)  
RUN r -e 'devtools::install_github("tidyverse/ggplot2")'  
  
## Add the build context to the root  
ADD . /asian_niche/  

