FROM python:3.4-slim  
  
MAINTAINER njordan.hsr@gmail.com  
  
ENV LANG en_US.utf8  
  
# install geodjango dependencies:
https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/geolibs/  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y\  
binutils\  
libgeos-dev\  
libproj-dev\  
gdal-bin\  
libsqlite3-dev\  
libspatialite-dev\  
libgeoip1\  
gdal-bin\  
python-gdal\  
gettext\  
virtualenv  

