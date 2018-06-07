FROM ubuntu:latest  
  
MAINTAINER Leonard Marschke <github@marschke.me>  
  
# update software repos  
RUN apt-get update \  
# ugrade software  
&& apt-get -y upgrade \  
&& apt-get -y install apt-utils \  
# install some useful tools need to build grml (git is needed to use with
gitlab ci)  
&& apt-get -y install \  
# install essential build tools  
git \  
build-essential \  
# python  
pyflakes \  
# C/C++  
make \  
cmake \  
libnetfilter-queue-dev \  
gcc \  
g++ \  
cppcheck \  
libcurlpp-dev \  
libcurl4-openssl-dev \  
libjson0 libjson0-dev \  
curl \  
# PHP  
php \  
php-gd \  
# Java  
openjdk-8-jdk \  
gradle \  
# other important packages  
fuse \  
wget \  
# filesystem test suite  
fio \  
# gource  
gource \  
libav-tools \  
imagemagick \  
xvfb \  
libwww-perl \  
# clean up  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

