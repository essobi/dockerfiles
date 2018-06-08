# Galaxy - requirements according to
https://wiki.galaxyproject.org/Admin/Config/ToolDependenciesList  
#  
# VERSION 2015.1  
  
FROM ubuntu:14.04  
  
MAINTAINER Björn A. Grüning, Dave Bouvier  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update && apt-get install --no-install-recommends -y apt-
transport-https software-properties-common && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 && \  
apt-get update -qq && apt-get upgrade -y && \  
add-apt-repository ppa:fkrull/deadsnakes && apt-get -qq update && \  
apt-get purge -y software-properties-common && \  
apt-get install --no-install-recommends -y autoconf automake build-essential
gfortran cmake \  
git-core libatlas-base-dev libblas-dev liblapack-dev openssl \  
openjdk-7-jre-headless python-dev python2.6 python2.6-dev python-setuptools \  
python-virtualenv zlib1g-dev libyaml-dev subversion python-dev pkg-config && \  
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  

