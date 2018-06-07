  
FROM debian:jessie  
MAINTAINER Marcel  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y gcc \  
gfortran \  
git \  
python-dev \  
libblas-dev \  
liblapack-dev \  
libpangocairo-1.0 \  
python-pip \  
python-dev \  
build-essential \  
libxml2 \  
libxml2-dev \  
libxslt1.1 \  
libxslt1-dev \  
zlib1g-dev \  
&& pip install --upgrade pip \  
&& pip install --upgrade virtualenv \  
&& pip install numpy \  
&& git clone https://github.com/mittagessen/kraken \  
&& cd kraken \  
&& pip install .  
&& cd .. \  
&& kraken get fraktur \  
&& kraken get omnibus \  
&& apt-get purge --auto-remove -y autoconf \  
build-essential \  
git \  
libleptonica-dev \  
libtool \  
&& rm -rf kraken /var/cache/apk/*  

