FROM ubuntu:16.04  
MAINTAINER Ronan Gill <ronan.gill@code.red>  
  
  
RUN apt-get update && \  
apt-get -yq dist-upgrade && \  
apt-get install -yq vim-tiny curl wget software-properties-common git htop man
unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo Europe/London > /etc/timezone && \  
dpkg-reconfigure tzdata && \  
locale-gen en_GB.UTF-8  
  
ENV LANG en_GB.UTF-8  
ENV LANGUAGE $LANG  
ENV LC_ALL $LANG  
ENV DISTRIB_ID Ubuntu  
ENV DISTRIB_RELEASE 16.04  
ENV DISTRIB_CODENAME xenial  
  
  
CMD /bin/bash  

