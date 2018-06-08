#  
# Julia Dockerfile  
#  
# https://github.com/mixxen/dockerfile  
#  
# Pull base image.  
FROM ubuntu:14.04  
  
RUN \  
apt-get update && \  
apt-get install -y python-numpy python-scipy python-matplotlib ipython
ipython-notebook python-pandas python-sympy python-nose python-pip && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y  
  
# Define working directory.  
WORKDIR /workspace  
  
CMD ["ipython"]  

