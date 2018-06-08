#  
# Julia Dockerfile  
#  
# https://github.com/mixxen/dockerfile  
#  
# Pull base image.  
FROM ubuntu:14.04  
  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository -y ppa:staticfloat/juliareleases && \  
add-apt-repository -y ppa:staticfloat/julia-deps && \  
apt-get update && \  
apt-get install -y julia && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get remove -y software-properties-common python-software-properties && \  
apt-get autoremove -y  
  
# Define working directory.  
WORKDIR /workspace  
  
CMD ["julia"]  
  

