FROM osmtw/ubuntu:xenial  
MAINTAINER Rex Tsai <rex.cc.tsai@gmail.com>  
  
ENV GDAL_VERSION=1.11.3+dfsg-3build2 \  
POSTGIS_VERSION=2.2.1+dfsg-2  
RUN apt-get install -y \  
gdal-bin=$GDAL_VERSION \  
python-gdal=$GDAL_VERSION \  
postgis=$POSTGIS_VERSION \  
ogdi-bin \  
proj-bin \  
pktools  
  
# Clean up APT when done  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

