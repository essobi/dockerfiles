FROM debian:wheezy  
  
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
libgeos-3.3.3 \  
libgeos-dev \  
python-yaml  
  
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
paver  
  
RUN wget https://www.dropbox.com/s/ufvffv2lpbn21vx/dbfpy-2.3.0.tar.gz && pip
install dbfpy-2.3.0.tar.gz  
  

