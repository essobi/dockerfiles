# vim:set ft=dockerfile:  
# VERSION 1.0  
# AUTHOR: Alexander Turcic <alex@zeitgeist.se>  
# DESCRIPTION: Claws Mail in a Docker container  
# TO_BUILD: docker build --rm -t zeitgeist/docker-claws .  
# SOURCE: https://github.com/alexzeitgeist/docker-claws  
# Pull base image.  
FROM debian:jessie  
MAINTAINER Alexander Turcic "alex@zeitgeist.se"  
RUN \  
apt-get update && \  
apt-get install -y \  
ca-certificates \  
claws-mail \  
fonts-dejavu \  
fonts-droid \  
libcanberra-gtk-module && \  
rm -rf /var/lib/apt/lists/*  
  
# Setup user environment. Replace 1000 with your user / group id.  
RUN \  
export uid=1000 gid=1000 && \  
groupadd --gid ${gid} user && \  
useradd --uid ${uid} \--gid ${gid} \--create-home user  
  
USER user  
WORKDIR /home/user  
VOLUME /home/user  
  
CMD ["/usr/bin/claws-mail"]  

