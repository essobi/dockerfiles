############################################################  
# Dockerfile to build kn_builder  
############################################################  
  
# Set the base image to ubuntu  
FROM ubuntu:14.04  
  
# File Author / Maintainer  
MAINTAINER Charles Blatti <blatti@illinois.edu>  
  
RUN apt-get update && apt-get -y install \  
build-essential \  
pkg-config \  
python3-numpy \  
python3-scipy \  
git-core \  
mysql-client \  
time \  
curl \  
rsync \  
wget  
  
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py  
  
RUN pip3 install https://cdn.mysql.com/Downloads/Connector-Python/mysql-
connector-python-2.0.4.tar.gz  
RUN pip3 install redis \  
requests \  
awscli \  
PyYAML  
  
ENV PYTHONUNBUFFERED 1  
  
COPY ./ /kn_builder/  
  
# Set default contain command on run  
CMD /bin/bash  
  
# Set container execution behavior  
# ENTRYPOINT  

