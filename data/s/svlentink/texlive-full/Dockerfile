# GPLv3  
FROM debian:latest  
  
# https://github.com/phusion/baseimage-docker/issues/58  
# http://serverfault.com/questions/618994/when-building-from-dockerfile-
debian-ubuntu-package-install-debconf-noninteract  
ENV DEBIAN_FRONTEND noninteractive  
  
# runs during installation and remove junk, as described in
http://docs.docker.com/engine/articles/dockerfile_best-practices/#apt-get  
RUN apt-get update && \  
apt-get install -y \  
texlive-full \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN rm -rf /usr/share/doc/ # delete 1.5GB of docs  

