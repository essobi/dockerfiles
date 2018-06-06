# docker for s2p  
# Gabriele Facciolo <gfacciol@gmail.com>  
# Carlo de Franchis <carlodef@gmail.com>  
FROM ubuntu:16.04  
MAINTAINER Carlo de Franchis <carlodef@gmail.com>  
RUN apt-get update && apt-get install -y \  
cmake \  
g++ \  
gcc \  
gdal-bin \  
git \  
libfftw3-dev \  
libgdal-dev \  
libgeotiff-dev \  
libtiff5-dev \  
libtiff-tools \  
libxslt1-dev \  
make \  
python \  
python-gdal \  
python-numpy \  
python-pip  
RUN pip install -U pip  
RUN pip install utm bs4 lxml  
  
# install s2p  
ADD s2p_docker_key /  
RUN chmod 600 /s2p_docker_key && echo "IdentityFile /s2p_docker_key" >>
/etc/ssh/ssh_config && echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config  
RUN git clone git@github.com:carlodef/s2p-iarpa.git --branch master --single-
branch --depth 1 s2p  
RUN cd s2p && make  
  
WORKDIR /s2p  

