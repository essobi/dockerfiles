FROM ubuntu:14.04  
# disable interactive functions  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y unzip wget curl dnsutils vim lsof
strace  
  
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

