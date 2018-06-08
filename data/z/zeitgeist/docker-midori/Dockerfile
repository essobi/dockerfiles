# vim:set ft=dockerfile:  
# VERSION 1.0  
# AUTHOR: Alexander Turcic <alex@zeitgeist.se>  
# DESCRIPTION: Midori browser in a Docker container  
# TO_BUILD: docker build --rm -t zeitgeist/docker-midori .  
# SOURCE: https://github.com/alexzeitgeist/docker-midori  
# Pull base image.  
FROM debian:jessie  
MAINTAINER Alexander Turcic "alex@zeitgeist.se"  
ENV DOWNLOAD_URL http://midori-
browser.org/downloads/midori_0.5.11-0_amd64_.deb  
  
RUN \  
sed -i 's/http.debian.net/ftp.ch.debian.org/' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y \  
ca-certificates \  
fonts-dejavu \  
gnome-icon-theme \  
libcanberra-gtk-module \  
wget && \  
wget "${DOWNLOAD_URL}" -O midori.deb && \  
{ dpkg -i midori.deb || true; } && \  
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
  
CMD ["/usr/bin/midori"]  

