FROM ubuntu:14.04  
MAINTAINER Michael Smith <mike@spokefire.co.uk>  
  
# Non interactive  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
# UTF8 OS!  
RUN locale-gen --no-purge en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get update && apt-get upgrade -y  

