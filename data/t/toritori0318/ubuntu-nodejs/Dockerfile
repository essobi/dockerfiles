FROM ubuntu:latest  
  
MAINTAINER TSUYOSHI TORII toritori0318  
  
# source list  
RUN echo 'deb http://jp.archive.ubuntu.com/ubuntu trusty main restricted' \  
&& echo 'deb-src http://jp.archive.ubuntu.com/ubuntu trusty main restricted' \  
&& echo 'deb http://jp.archive.ubuntu.com/ubuntu trusty-updates main
restricted' \  
&& echo 'deb-src http://jp.archive.ubuntu.com/ubuntu trusty-updates main
restricted'  
  
# packages  
RUN apt-get -q -y update \  
&& apt-get -q -y install git wget tar gzip build-essential python-dev \  
&& apt-get -q -y install curl nodejs-legacy npm \  
&& apt-get -q -y clean && rm -rf /var/cache/apt/archives/*
/var/lib/apt/lists/*  
  
# pip  
RUN curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py |
python  
  
# node cli  
RUN npm install -g grunt-cli gulp  

