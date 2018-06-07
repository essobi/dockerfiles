# Docker container for delve, a probabilistic short read aligner used in
FANTOM5 and ENCODE  
# See http://fantom.gsc.riken.jp/jp/software/  
# VERSION 0.1  
# Pull base image.  
FROM debian:stable  
  
# :)  
MAINTAINER Tazro Inutano Ohta, inutano@gmail.com  
  
# Install packages via apt-get.  
RUN apt-get update && \  
apt-get install -y wget gcc make && \  
rm -rf /var/lib/apt/lists/*  
  
# Download and unpack  
WORKDIR /  
RUN wget "http://fantom.gsc.riken.jp/5/suppl/delve/delve.tgz" && \  
tar zxfv delve.tgz && \  
cd /delve && \  
make && cp /delve/src/delve /bin  
  
# Define working directory.  
WORKDIR /data  
  
# Default command  
CMD ["delve"]  

