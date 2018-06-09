# -*- coding: utf-8 -*-  
  
FROM buildpack-deps:wheezy  
  
MAINTAINER Aleksandr Zykov <tiger@vilijavis.lt>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN ( \  
apt-get update -q \  
&& apt-get upgrade -qy --no-install-recommends \  
&& apt-get clean -qy \  
)  
  
RUN ( \  
apt-get install -qy --no-install-recommends \  
ca-certificates \  
&& apt-get clean -qy \  
)  
  
RUN ( \  
apt-get install -qy --no-install-recommends \  
aptitude \  
lsb-release \  
python-pip \  
python-dev \  
libxml2-dev \  
libxslt-dev \  
coreutils \  
dnsutils \  
iputils-ping \  
net-tools \  
iptables \  
figlet \  
wget \  
curl \  
bzip2 \  
unzip \  
zip \  
&& apt-get clean -qy \  
)  
  
RUN ( \  
pip install --upgrade pip \  
&& /usr/local/bin/pip install -U setuptools \  
&& /usr/local/bin/pip install \  
ansible \  
)  
  
RUN ansible --version  
  
RUN figlet 'Ready!'  

