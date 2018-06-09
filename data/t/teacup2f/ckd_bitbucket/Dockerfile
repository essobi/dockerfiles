#A working env for CKD project with latest scipy,numpy,sklearn and meteor  
FROM ubuntu:14.04  
MAINTAINER Evan Li <evan@zhmed.com>  
  
#install python prerequisites  
RUN sudo apt-get update && apt-get install -y python-pip build-essential
python-dev python-setuptools \  
python-numpy python-scipy \  
libatlas-dev libatlas3gf-base  
RUN sudo update-alternatives --set libblas.so.3 \  
/usr/lib/atlas-base/atlas/libblas.so.3  
RUN sudo update-alternatives --set liblapack.so.3 \  
/usr/lib/atlas-base/atlas/liblapack.so.3  
RUN sudo pip install -U sklearn  
  
#install meteor prerequisites  
RUN sudo apt-get -y install curl  
RUN curl https://install.meteor.com/ | sh  
  

