FROM uribo/tiny_rocker_minimum:latest  
MAINTAINER "Shinya Uryu" r.sh1nya.uryu@gmail.com  
  
RUN apt-get install -y --no-install-recommends \  
libudunits2-dev \  
libgdal-dev  
  
RUN install2.r \  
leaflet raster rasterVis sf lwgeom stplanr  

