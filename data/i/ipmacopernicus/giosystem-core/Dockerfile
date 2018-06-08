# This docker file deploys giosystem-core in a new docker image  
# docker build -t ricardogsilva/giosystem-core:latest .  
FROM ubuntu:16.04  
MAINTAINER Ricardo Garcia Silva  
LABEL Description="This image builds giosystem-core"  
RUN apt-get update && apt-get install -y \  
build-essential \  
cgi-mapserver \  
gdal-bin \  
git \  
libgdal-dev \  
libffi-dev \  
libxml2 \  
libxml2-dev \  
libxslt1.1 \  
libxslt1-dev \  
python \  
python-dev \  
python-gdal \  
python-mapscript \  
python-numpy \  
python-numexpr \  
python-h5py \  
wget  
RUN wget https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install --upgrade pip setuptools pyOpenSSL requests[security]  
COPY . /tmp/giosystem-core  
WORKDIR /tmp/giosystem-core  
RUN pip install --requirement requirements.txt  
WORKDIR /tmp  
RUN pip install --editable giosystem-core  

