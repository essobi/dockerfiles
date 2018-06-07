FROM stackbrew/ubuntu:saucy  
MAINTAINER james@lazyatom.com  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu saucy main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y ca-certificates vim-tiny wget bzip2 software-
properties-common git-core  
RUN locale-gen en_US.UTF-8  
RUN echo "export LC_ALL=en_US.UTF-8" >> /etc/bash.bashrc  
RUN echo "export LANG=en_US.UTF-8" >> /etc/bash.bashrc  
ENV LANG en_US.UTF-8  

