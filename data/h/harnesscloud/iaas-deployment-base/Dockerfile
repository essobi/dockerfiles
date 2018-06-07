FROM phusion/baseimage:latest  
MAINTAINER Gabriel Figueiredo <gabriel.figueiredo@imperial.ac.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install \  
curl \  
git \  
libzmq-dev \  
python-dev \  
python-glpk \  
python-nova \  
python-neutron \  
python-pip && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN pip install \  
bottle \  
flask-classy \  
Flask \  
psutil \  
pyzmq \  
supervisor  

