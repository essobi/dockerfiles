FROM edyan/full-lamp:5.6  
MAINTAINER Emmanuel Dyan <emmanueldyan@gmail.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN echo "deb http://http.debian.net/debian jessie-backports main contrib non-
free" >> /etc/apt/sources.list.d/jessie-backports.list  
  
# Upgrade the system and Install GIT and Libreoffice  
RUN apt-get update && \  
apt-get upgrade -y && \  
# Install required packages  
apt-get install -t jessie-backports -y --no-install-recommends libreoffice-
writer && \  
# Clean  
apt-get autoremove -y && \  
apt-get autoclean && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /usr/share/man/* /usr/share/doc/* /var/cache/*
/var/log/*  

