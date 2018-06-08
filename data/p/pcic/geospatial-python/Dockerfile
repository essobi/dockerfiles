FROM ubuntu:17.10  
  
MAINTAINER James Hiebert <hiebert@uvic.ca>  
  
RUN apt-get update && \  
apt-get -yq install \  
libhdf5-dev \  
libnetcdf-dev \  
libgdal-dev \  
libyaml-dev \  
python \  
python-dev \  
python-pip \  
python-virtualenv \  
cython \  
python3 \  
python3-dev \  
python3-pip \  
cython3 && \  
rm -rf /var/lib/apt/lists/*  
  
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal  
ENV C_INCLUDE_PATH=/usr/include/gdal  
  
RUN pip install numpy && pip3 install numpy  
  
RUN pip install gdal==2.2 h5py netCDF4 psycopg2 PyYAML pillow  
  
RUN pip3 install gdal==2.2 h5py netCDF4 psycopg2 PyYAML pillow  

