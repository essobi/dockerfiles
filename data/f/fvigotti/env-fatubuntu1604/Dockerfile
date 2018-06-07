FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV TERM xterm  
  
RUN apt-get -y update && \  
apt-get -y --quiet upgrade && \  
apt-get -y --quiet install libxml2-dev libxslt1-dev git python python-
setuptools python-dev build-essential libz-dev lsb openssl dnsutils curl rsync
iptraf-ng rdiff ethtool iotop libtool pv curl unzip zip inotify-tools && \  
apt-get -y --quiet install python-software-properties software-properties-
common htop pwgen npm nodejs-legacy nodejs gcc libc6-dev make wget vim nano
mariadb-client jq optipng pngquant xvfb cifs-utils zstd inotify-tools&& \  
easy_install pip && \  
pip --no-input install envtpl && \  
apt-get -y update && \  
apt-get -y clean  
  
RUN useradd -u 500 core  
  
  
  

