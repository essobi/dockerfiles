# ImageMagick-Full  
# Author: Sean Matheson  
# Version: 0.0.2  
# Repo: https://bitbucket.org/acleancoder/imagemagick-full  
# Docker Hub: https://registry.hub.docker.com/u/acleancoder/imagemagick-full/  
FROM ubuntu:14.04.1  
# This prevents us from get errors during apt-get installs as it notifies the  
# environment that it is a non-interactive one.  
ENV DEBIAN_FRONTEND noninteractive  
  
# TRUSTY-BACKPORTS  
# We all the trusty-backports source as this will give us access to a povray  
# package. Not having to build this package from source great decreases the  
# final size of the container.  
RUN \  
echo "deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted
universe multiverse" >> /etc/apt/sources.list  
  
# POVRAY  
RUN \  
apt-get update && \  
apt-get -y install \  
povray=1:3.7.0.0-4~ubuntu14.04.1 && \  
rm -rf /var/lib/apt/lists/*  
  
# IMAGEMAGICK  
# Install all the recommended and suggested packages for ImageMagick  
RUN \  
apt-get update && \  
apt-get -y install \  
imagemagick gmic  
  
# Clean the cache created by package installations  
RUN \  
apt-get clean  

