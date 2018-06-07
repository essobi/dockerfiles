# Taking as base image a Ubuntu Desktop container with web-based noVNC
connection enabled  
FROM rupertnash/vmtk-docker  
MAINTAINER Miguel O. Bernabeu (miguel.bernabeu@ed.ac.uk)  
  
##  
# Dependencies  
##  
# OpenMPI in Universe  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe"
&& \  
apt-get update  
  
RUN apt-get install -y \  
git \  
python-wxtools \  
python-wxversion \  
swig  
  
RUN pip install \  
cython \  
numpy \  
PyYAML  

