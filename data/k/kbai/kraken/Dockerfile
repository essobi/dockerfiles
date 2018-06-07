FROM ubuntu:16.04  
MAINTAINER Konstantin Baierer <konstantin.baierer@gmail.com>  
ENV PBR_VERSION 0.8.0  
ENV DEBIAN_FRONTEND noninteractive  
ENV PYTHONIOENCODING utf8  
  
WORKDIR /kraken  
  
ADD kraken /kraken  
RUN apt-get update && apt-get -y install --no-install-recommends \  
ca-certificates \  
gcc \  
python-pip \  
python-setuptools \  
python-dev \  
python-pip \  
python-setuptools \  
python-scipy \  
python-numpy \  
python-pil \  
python-click \  
python-lxml \  
&& pip install --upgrade pip \  
&& pip install pbr \  
&& pip install -r requirements.txt \  
&& pip install . \  
&& kraken get default \  
&& kraken get fraktur \  
&& apt-get -y remove --purge --auto-remove \  
gcc \  
python-pip \  
python-setuptools \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* .git  
  
WORKDIR /data  
  
ENTRYPOINT ["/usr/local/bin/kraken"]  

