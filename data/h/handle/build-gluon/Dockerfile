FROM debian:stable-slim  
  
# Set locale  
ENV LANG C.UTF-8  
# Make configure ignore root  
ENV FORCE_UNSAFE_CONFIGURE 1  
# Install needed packages  
RUN apt-get update && apt-get install -y bzip2 gawk g++ gcc git
libncurses5-dev libssl-dev make python unzip wget zlib1g-dev  
  
# Fetch files from gluon repository  
RUN git clone https://github.com/freifunk-gluon/gluon.git gluon  

