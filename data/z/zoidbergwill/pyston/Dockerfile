# Dockerfile for Pyston  
FROM debian:jessie  
MAINTAINER William Stewart <zoidbergwill@gmail.com>  
  
ENV LANG=C.UTF-8 DEBIAN_FRONTEND=noninteractive  
  
RUN set -e; \  
umask 0022; \  
apt-get update; apt-get -yq install wget libsqlite3-0 libgmp10 libatomic1
openssl; \  
wget -O - -q
https://github.com/dropbox/pyston/releases/download/v0.4/pyston-0.4.0-linux64.tar.gz
| \  
tar -xzC /usr/local; \  
mkdir -p /usr/local/from_cpython/Lib/; \  
cp -R /usr/local/pyston-0.4.0-linux64/virtualenv/*
/usr/local/from_cpython/Lib; \  
ln -s /usr/local/pyston-0.4.0-linux64/pyston /usr/local/bin/; \  
apt-get purge -yq wget; \  
apt-get autoclean -y; \  
apt-get autoremove -y; \  
rm -rf /usr/share/locale/*; \  
rm -rf /var/cache/debconf/*-old; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; \  
rm -rf /usr/share/doc/*  
  
CMD ["pyston"]  

