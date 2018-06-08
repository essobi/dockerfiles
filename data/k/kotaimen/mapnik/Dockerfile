FROM ubuntu:bionic  
MAINTAINER Kotaimen <kotaimen.c@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#  
# Install packages  
#  
RUN set -x \  
&& apt-get -q update \  
&& apt-get -yq --no-install-recommends install \  
locales \  
ca-certificates \  
curl \  
build-essential \  
gcc \  
imagemagick \  
libmapnik3.0 \  
mapnik-utils \  
\  
python3 \  
cython3 \  
python3-pip \  
python3-wheel \  
python3-setuptools \  
python3-dev \  
python3-pil \  
python3-numpy \  
python3-scipy \  
python3-pylibmc \  
python3-skimage \  
python3-gdal \  
python3-mapnik \  
python3-lxml \  
\  
npm  
#  
# Install carto  
#  
RUN set -x \  
&& npm install -g carto millstone  
  
#  
# Patch missing gdal data file  
#  
RUN curl -sSL https://github.com/OSGeo/gdal/raw/2.2/gdal/data/esri_extra.wkt >
\  
/usr/share/gdal/2.2/esri_extra.wkt  
  

