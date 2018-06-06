# vim:set ft=dockerfile:  
# VERSION 1.0  
# AUTHOR: Alexander Turcic <alex@zeitgeist.se>  
# DESCRIPTION: sslyze in a Docker container  
# TO_BUILD: docker build --rm -t zeitgeist/docker-sslyze .  
# SOURCE: https://github.com/alexzeitgeist/docker-sslyze  
# Pull base image.  
FROM debian:jessie  
MAINTAINER Alexander Turcic "alex@zeitgeist.se"  
# Compile sslyze  
RUN \  
apt-get update && \  
apt-get install -y git build-essential && \  
git clone https://github.com/rbsec/sslscan.git && \  
cd sslscan && \  
make static && \  
make install && \  
cd / && \  
rm -rf /sslscan && \  
apt-get purge -y git build-essential && \  
apt-get -y autoremove --purge && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
export uid=1000 gid=1000 && \  
groupadd --gid ${gid} user && \  
useradd --uid ${uid} \--gid ${gid} \--create-home user  
  
USER user  
WORKDIR /home/user  
  
ENTRYPOINT ["/usr/bin/sslscan"]  

