FROM jupyter/datascience-notebook:cf6258237ff9  
  
USER root  
  
# Install needed packages.  
RUN \  
export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -q \  
&& apt-get install -q -y -o Dpkg:Options::="--force-confnew" \  
automake \  
build-essential \  
git \  
inotify-tools \  
libcurl4-openssl-dev \  
libfuse-dev \  
libssl-dev \  
libtool \  
libxml2-dev \  
mime-support \  
pkg-config \  
rsync  
  
# Install system support for the Python packages we will use.  
RUN \  
export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -q \  
&& apt-get install -q -y -o Dpkg:Options::="--force-confnew" \  
gdal-bin \  
libgdal-dev \  
libgeos-dev \  
libproj-dev \  
procps \  
python-dev \  
python-gdal \  
python-pip \  
vim  
  
# Update and install Python packages we will use.  
RUN \  
conda install -y \  
boto3 \  
geopandas \  
pyproj \  
shapely \  
tensorflow \  
theano  
  
# Default 'fiona' package is broken, use IOOS channel version instead.  
RUN conda install -c ioos fiona  
  
# ADD https://downloads.sourceforge.net/project/matplotlib/matplotlib-
toolkits/basemap-1.0.7/basemap-1.0.7.tar.gz /home/jovyan/basemap  
# ...or...  
# RUN \  
# mkdir -p /home/jovyan/basemap \  
# && curl -SL https://downloads.sourceforge.net/project/matplotlib/matplotlib-
toolkits/basemap-1.0.7/basemap-1.0.7.tar.gz \  
# | tar -zxC /home/jovyan/basemap  
# ...or...  
# COPY lib/python/basemap-1.0.7.tar.gz /home/jovyan/basemap/  
# RUN tar zxf /home/jovyan/basemap/basemap-1.0.7.tar.gz -C
/home/jovyan/basemap  
#  
# RUN \  
# cd /home/jovyan/basemap/basemap-1.0.7 \  
# && ln /usr/lib/.gitignorelibgeos-3.4.2.so /usr/lib/libgeos.so \  
# && python setup.py install  
  
USER jovyan  

