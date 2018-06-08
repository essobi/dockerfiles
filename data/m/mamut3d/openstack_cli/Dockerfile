FROM ubuntu:xenial  
  
MAINTAINER Mamut3D  
  
LABEL Description="Openstack client tools"  
  
RUN apt-get update && apt-get install -y \  
locales \  
apt-utils \  
mc \  
vim \  
iputils-ping \  
python-dev \  
python-pip \  
python-setuptools \  
ca-certificates \  
gcc \  
libssl-dev \  
musl-dev \  
&& pip install --upgrade --no-cache-dir pip setuptools python-openstackclient
python-keystoneclient \  
&& pip install --upgrade --no-cache-dir python-heatclient python-neutronclient
python-ceilometerclient shade \  
&& pip install os-client-config==1.26.0 \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG en_US.utf8  
CMD ["/bin/bash"]  

