FROM ubuntu:latest  
  
MAINTAINER Jakub Gruszecki <gruszecki.jakub@gmail.com>  
  
RUN apt-get -y update && \  
apt-get -y install man && \  
apt-get -y install emacs && \  
apt-get -y install sudo && \  
apt-get -y install less && \  
apt-get -y install binutils && \  
apt-get -y install vim-common && \  
apt-get -y install file && \  
apt-get -y install mlocate  
  
COPY sample/* home/  
  
ENTRYPOINT /bin/bash

