#  
# Octave Dockerfile  
#  
# https://github.com/mixxen/dockerfile  
#  
# Pull base image.  
FROM ubuntu:14.04  
  
RUN \  
apt-get update && \  
apt-get install -y octave && \  
apt-get -y install epstool && \  
apt-get -y install transfig && \  
rm -rf /var/lib/apt/lists/*  
# Define working directory.  
WORKDIR /workspace  
  
CMD ["octave"]  

