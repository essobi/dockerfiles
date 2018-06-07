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
  
# FFMPEG  
# We install ffmpeg using a respected PPA by Jon Severinsson. This PPA is  
# well maintained and recommended by the official ffmpeg website. It builds  
# ffmpeg in a shared library mode with all it's dependencies included.  
RUN \  
apt-get update && \  
apt-get -y install \  
software-properties-common=0.92.37.2 && \  
apt-add-repository -y ppa:jon-severinsson/ffmpeg && \  
apt-get update && \  
apt-get -y install \  
ffmpeg=7:1.2.6-1~trusty1 && \  
rm -rf /var/lib/apt/lists/*  
  
# IMAGEMAGICK  
# Install all the recommended and suggested packages for ImageMagick  
RUN \  
apt-get update && \  
apt-get -y install \  
ghostscript=9.10~dfsg-0ubuntu10.2 \  
libmagickcore5-extra=8:6.7.7.10-6ubuntu3 \  
netpbm=2:10.0-15ubuntu2 \  
autotrace=0.31.1-16build2 \  
cups-bsd=1.7.2-0ubuntu1.2 \  
curl=7.35.0-1ubuntu2.2 \  
enscript=1.6.5.90-2 \  
gimp=2.8.10-0ubuntu1 \  
grads=2:2.0.1-1build1 \  
groff-base=1.22.2-5 \  
hp2xx=3.4.4-9 \  
html2ps=1.0b7-1 \  
libwmf-bin=0.2.8.4-10.3ubuntu1 \  
mplayer=2:1.1+dfsg1-0ubuntu3 \  
radiance=4R1+20120125-1.1 \  
sane-utils=1.0.23-3ubuntu3.1 \  
texlive-binaries=2013.20130729.30972-2build3 \  
transfig=1:3.2.5.e-1ubuntu1 \  
ufraw-batch=0.19.2-2ubuntu2 \  
xdg-utils=1.1.0~rc1-2ubuntu7.1 && \  
apt-get -y install \  
gnuplot=4.6.4-2 \  
imagemagick-doc=8:6.7.7.10-6ubuntu3 \  
imagemagick=8:6.7.7.10-6ubuntu3 && \  
rm -rf /var/lib/apt/lists/*  
  
# Clean the cache created by package installations  
RUN \  
apt-get clean  

