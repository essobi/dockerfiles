FROM ubuntu:14.04.5  
MAINTAINER Maciej Olędzki <maciej.oledzki@gmail.com>  
  
# Set locale  
RUN locale-gen --no-purge en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y --fix-missing wget ca-certificates
gettext-base && rm -rf /var/lib/apt/lists/*  

