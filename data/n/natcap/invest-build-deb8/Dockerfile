# InVEST build image for Docker.  
# Docker image to install all required packages to be able to build  
# InVEST binaries on debian:jessie.  
  
FROM debian:jessie  
  
RUN apt-get update && apt-get install -y \  
wget \  
git \  
zip \  
mercurial \  
subversion \  
gdal-bin \  
python-gdal \  
python-qt4 \  
python-numpy \  
python-scipy \  
libgeos-3.4.2 \  
libgeos-dev  
  
# install pip and needed python packages  
RUN wget --no-check-certificate 'http://bootstrap.pypa.io/get-pip.py' &&
python get-pip.py  
  
RUN pip install --upgrade setuptools  
RUN pip install \  
cython \  
shapely \  
python-dateutil \  
pyparsing \  
six \  
pyamg \  
poster \  
nose \  
tox \  
fabric \  
mock \  
paver \  
pyyaml  
  
RUN wget https://www.dropbox.com/s/ufvffv2lpbn21vx/dbfpy-2.3.0.tar.gz && pip
install dbfpy-2.3.0.tar.gz  
  
RUN adduser --home /home/jenkins jenkins  
USER jenkins  
WORKDIR /home/jenkins  

