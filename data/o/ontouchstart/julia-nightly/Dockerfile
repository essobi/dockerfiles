FROM ubuntu:14.04  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update -y  
RUN apt-get install software-properties-common python-software-properties -y  
RUN add-apt-repository ppa:staticfloat/julianightlies -y  
RUN add-apt-repository ppa:staticfloat/julia-deps -y  
RUN apt-get update -y  
RUN apt-get install julia -y  
RUN julia --version  

