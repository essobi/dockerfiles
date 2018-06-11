FROM ubuntu:xenial  
MAINTAINER Michael Ruettgers <mr@westwerk.ac>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Copy image related files  
COPY files/ /  
  
# Cleanup  
RUN rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/man/* && \  
rm -rf /usr/share/locale/*  
  
# Define packages to be installed  
ENV PACKAGES \  
vim \  
less \  
bzip2 \  
rsync  
  
# Install packages && cleanup  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get -y install $PACKAGES  

