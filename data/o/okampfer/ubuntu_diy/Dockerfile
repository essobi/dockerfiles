FROM ubuntu:16.04  
MAINTAINER Bruce Sun <okampfer@gmail.com>  
  
RUN apt-get update && \  
apt-get -y install sudo software-properties-common  
  
RUN adduser --disabled-password --gecos '' athrun && \  
adduser athrun sudo  
  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
RUN mkdir /home/athrun/Downloads  
  
ENV USER=athrun  
USER athrun  
CMD /bin/bash  

