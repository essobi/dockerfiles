#####  
# Dockerfile for MedPy - Medical image processing in Python  
# https://pypi.python.org/pypi/MedPy/  
# https://github.com/loli/medpy  
#  
# Docker container building with the development version of MedPy found at
GitHub.  
# Installs MedPy in development mode (i.e. changes made to the library
immediately become visible system wide) in /root/medpy.  
# version 0.1  
# created 2014-12-07  
#####  
FROM loli/medpy:dependencies  
  
MAINTAINER Oskar Maier <oskar.maier@googlemail.com>, Dirk Fortmeier  
  
# install MedPy development version  
RUN apt-get install -y git  
RUN mkdir /root/medpy  
WORKDIR /root/medpy  
RUN git clone https://github.com/loli/medpy.git .  
RUN python setup.py develop  
  

