FROM ubuntu:15.10  
MAINTAINER CT Cheng <chintzung@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y make wget zlib1g-dev g++
libcrypto++-dev  
RUN wget https://limitingfactor.urbackup.org/Client/2.0.20%20beta/urbackup-
client-2.0.20.0.tar.gz  
RUN tar -zxvf urbackup-client-2.0.20.0.tar.gz  
WORKDIR urbackup-client-2.0.20.0  
RUN /bin/bash -c './configure --enable-headless'  
RUN /bin/bash -c 'make'  
RUN /bin/bash -c 'make install'  
WORKDIR /  
RUN rm -rf urbackup-client-2.0.20.0  
RUN rm urbackup-client-2.0.20.0.tar.gz  
RUN apt-get remove -y make wget g++  
RUN apt-get clean  

