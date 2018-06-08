FROM ubuntu:14.04.1  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update  
RUN apt-get -qy upgrade  
RUN apt-get install -qy python-software-properties software-properties-common  
RUN add-apt-repository ppa:snappy-dev/beta  
RUN apt-get update  
RUN apt-get install -qy snappy-tools bzr  
RUN snappy -v  
RUN snappy -h  
  
ENV HOME /home  
WORKDIR /home  

