FROM ubuntu:14.04  
MAINTAINER Isidoro Legido "islegmar@gmail.com"  
RUN apt-get update && apt-get -y upgrade  
  
RUN apt-get -y install \  
wget \  
build-essential \  
libreadline-dev \  
flex \  
libncurses-dev \  
libplot-dev  
  
RUN wget http://tph.tuwien.ac.at/~oemer/tgz/qcl-0.6.4.tgz  
RUN tar xvzf qcl-0.6.4.tgz  
RUN cd qcl-0.6.4 && make  
  

