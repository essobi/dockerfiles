FROM ubuntu:bionic  
  
MAINTAINER Leonard Marschke <github@marschke.me>  
  
# Set pythonunbuffered for getting better outputs in combination with GitLab
CI  
ENV PYTHONUNBUFFERED=1  
# Set noninteractive environment  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Set language environment to UTF-8  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
# install build dependencies  
RUN apt-get update \  
# ugrade software  
&& apt-get -y upgrade \  
&& apt-get -y install apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common \  
# clean up  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# Prepare docker-ce installation  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) edge" \  
# clean up  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# update software repos  
RUN apt-get update \  
# upgrade software  
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
python-requests \  
python3-pip \  
python-pip \  
python3-psycopg2 \  
libffi-dev \  
# C/C++  
make \  
cmake \  
libnetfilter-queue-dev \  
gcc \  
g++ \  
cppcheck \  
libcurlpp-dev \  
libcurl4-openssl-dev \  
libjson-c3 libjson-c-dev \  
curl \  
libssl-dev \  
librtmp-dev \  
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
# Docker  
docker-ce \  
# yasm (needed e.g. for ffmpeg)  
yasm \  
# fabric (deployment tool)  
fabric \  
# documentation creation \  
pandoc \  
# clean up  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

