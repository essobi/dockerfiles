FROM orchardup/python:2.7  
MAINTAINER Marc Abramowitz <marc@marc-abramowitz.com> (@msabramo)  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
freetds-bin \  
freetds-common \  
freetds-dev \  
gfortran \  
git \  
libatlas-dev \  
libatlas-base-dev \  
libblas-dev \  
libcurl4-openssl-dev \  
liblapack-dev \  
libmemcached-dev \  
libsasl2-dev \  
libxml2-dev \  
libxmlsec1 \  
libxslt1-dev \  
python-dev \  
python2.7-dev \  
silversearcher-ag \  
tree \  
vim \  
zlib1g-dev  
  
RUN pip install \  
bpython \  
Cython \  
gevent \  
gunicorn==18.0 \  
ipython \  
lxml \  
numpy \  
pandas \  
pdbpp \  
Pillow \  
pylibmc \  
pymssql \  
pyramid \  
pyzmq \  
scikit-learn \  
scipy \  
simplejson \  
SQLAlchemy \  
tornado \  
ujson  

