FROM phusion/baseimage  
MAINTAINER Adam K Dean <adamkdean@googlemail.com>  
  
# Update container with dependencies  
RUN apt-get update; \  
apt-get install -qy curl pkg-config python-software-properties python g++ make
software-properties-common; \  
apt-get clean; \  
apt-get autoremove;  
  
CMD ["bash"]  

