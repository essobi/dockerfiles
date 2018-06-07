# vim:set ft=dockerfile:  
# VERSION 1.0  
# AUTHOR: Alexander Turcic <alex@zeitgeist.se>  
# DESCRIPTION: Latest version of opera-beta in a Docker container  
# TO_BUILD: docker build --rm -t zeitgeist/docker-opera .  
# SOURCE: https://github.com/alexzeitgeist/docker-opera  
# Pull base image.  
FROM debian:jessie  
MAINTAINER Alexander Turcic "alex@zeitgeist.se"  
ENV DOWNLOAD_URL http://deb.opera.com/opera-beta/pool/non-free/o/opera-beta/  
  
RUN \  
apt-get update && \  
apt-get install -y \  
libcanberra-gtk-module \  
wget && \  
RELEASE=`wget -q -O - ${DOWNLOAD_URL} | grep -m 1 -o -E "opera-
beta[^<>]*?amd64.deb" | head -1` && \  
wget -r --no-parent "${DOWNLOAD_URL}${RELEASE}" -O opera.deb && \  
{ dpkg -i opera.deb || true; } && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y -f && \  
apt-get purge -y --auto-remove wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Setup user environment. Replace 1000 with your user / group id.  
RUN \  
export uid=1000 gid=1000 && \  
groupadd --gid ${gid} user && \  
useradd --uid ${uid} \--gid ${gid} \--create-home user  
  
USER user  
WORKDIR /home/user  
VOLUME /home/user  
  
CMD ["/usr/bin/opera-beta"]  

