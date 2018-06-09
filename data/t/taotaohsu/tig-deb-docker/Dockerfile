FROM debian:7.8  
MAINTAINER Taotao Hsu <taotaohsu@gmail.com>  
  
RUN apt-get update && \  
apt-get upgrade -y --force-yes && \  
apt-get install -y --force-yes \  
build-essential \  
wget \  
ca-certificates \  
automake \  
autoconf \  
libncurses5-dev \  
libncursesw5-dev \  
libreadline-dev \  
asciidoc \  
xmlto \  
docbook-utils \  
git \  
devscripts && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

