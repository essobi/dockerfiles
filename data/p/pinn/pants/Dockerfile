FROM pinn/pants:scientific  
  
# IAM dependencies  
RUN apt-get update && apt-get -y --no-install-recommends install \  
libtool \  
libxml2-dev \  
libxmlsec1-dev \  
libxmlsec1-openssl \  
libxslt1-dev \  
libssl-dev python-lxml \  
python-certifi \  
python-cffi \  
python-cryptography \  
python-defusedxml \  
python-openssl && \  
apt-get clean && \  
rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* /var/tmp/*  
  
RUN PEX_VERBOSE=5 ./pants pyprep src/python:iam

