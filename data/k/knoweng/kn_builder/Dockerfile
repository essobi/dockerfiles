############################################################  
# Dockerfile to build kn_builder  
############################################################  
  
# Set the base image to ubuntu  
FROM ubuntu:16.04  
  
# File Author / Maintainer  
MAINTAINER Charles Blatti <blatti@illinois.edu>  
  
RUN apt-get update && apt-get -y install \  
lxc \  
liblapack-dev \  
libblas-dev \  
gfortran \  
build-essential \  
python3-pip \  
python3-numpy \  
python3-scipy \  
redis-server \  
mysql-client \  
time \  
curl \  
rsync \  
wget  
  
RUN pip3 install https://cdn.mysql.com/Downloads/Connector-Python/mysql-
connector-python-2.0.4.tar.gz  
RUN pip3 install redis \  
requests \  
PyYAML  
  
ENV PYTHONUNBUFFERED 1  
  
COPY ./ /kn_builder/  
  
# Set default contain command on run  
CMD /bin/bash  
  
# Set container execution behavior  
# ENTRYPOINT  

