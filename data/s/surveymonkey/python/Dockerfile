FROM orchardup/python  
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
silversearcher-ag \  
tree \  
vim \  
zlib1g-dev  
  
RUN pip install \  
ansible \  
ansible-shell \  
bpython \  
Cython \  
gevent \  
gunicorn==18.0 \  
ipython \  
lxml \  
msgpack-python \  
numpy \  
pandas \  
pdbpp \  
Pillow \  
pylibmc \  
pycrypto \  
pymssql \  
pyramid \  
pyzmq \  
scikit-learn \  
scipy \  
simplejson \  
SQLAlchemy \  
tornado \  
ujson  
  
CMD ["ipython"]  

