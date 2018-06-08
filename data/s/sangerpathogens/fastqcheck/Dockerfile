#  
# Base-image  
#  
FROM debian:testing  
  
#  
# Authorship  
#  
MAINTAINER ap13@sanger.ac.uk  
  
#  
# A shared directory for results  
#  
VOLUME ["/data"]  
  
#  
# Pull in Debian Dependancies  
#  
RUN apt-get update -qq && apt-get -y install libc6 git automake libtool make  
  
#  
# Close master from github  
#  
RUN git clone https://github.com/sanger-pathogens/fastqcheck.git  
#  
# Build and install  
#  
RUN cd fastqcheck && autoreconf -i -f && ./configure && make && make install  
  
#  
# Make sure the library is accessible  
#  
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH  
  
#  
# Set the directory to be the shared dir  
#  
WORKDIR /data  

