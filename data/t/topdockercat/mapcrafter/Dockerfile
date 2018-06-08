FROM ubuntu:xenial  
  
MAINTAINER TopCat <topmailcat@googlemail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /  
  
# upgrade the system  
RUN apt-get update && apt-get -y upgrade  
  
# install depedencies  
RUN apt-get update && \  
apt-get -y install python curl wget apt-transport-https && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## add mapcrafter deb package repository.
https://docs.mapcrafter.org/builds/stable/installation.html#debian-packages  
RUN echo "deb http://packages.mapcrafter.org/ubuntu xenial main" | tee
/etc/apt/sources.list.d/mapcrafter.list && \  
wget -O /etc/apt/trusted.gpg.d/mapcrafter.gpg
http://packages.mapcrafter.org/ubuntu/keyring.gpg  
  
# install mapcrafter  
RUN apt-get update && \  
apt-get -y install mapcrafter && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# add sample render config  
ADD render.conf ./  
  
CMD ["mapcrafter", "-c", "./render.conf", "-j", "2"]  

