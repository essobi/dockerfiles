############################################################  
# Dockerfile to build bedops 2.4.26 container images  
# Based on Ubuntu adapted from Sophie Lemoine <slemoine@biologie.ens.fr>  
############################################################  
  
  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
  
# File Author / Maintainer  
MAINTAINER Jennifer Brody <jeco@uw.edu>  
  
# Update the repository sources list  
RUN apt-get update  
  
# Install compiler and perl stuff  
RUN apt-get install --yes \  
build-essential \  
gcc-multilib \  
apt-utils \  
zip \  
wget  
  
  
  
# Install bedops 2.4.26  
WORKDIR /usr/local/  
RUN mkdir bedops_v2.4.26  
WORKDIR /usr/local/bedops_v2.4.26  
RUN wget https://github.com/bedops/bedops/archive/master.zip  
RUN unzip master.zip  
WORKDIR /usr/local/bedops_v2.4.26/bedops-master  
RUN make  
RUN make install  
RUN cp bin/* /usr/local/bin/  
  
# Cleanup  
#RUN rm /usr/local/bedops_v2.4.1/bedops_linux_x86_64-v2.4.14.tar.bz2  
RUN apt-get clean  
RUN apt-get remove --yes --purge build-essential wget gcc-multilib apt-utils
zlib1g-dev vim-common  

