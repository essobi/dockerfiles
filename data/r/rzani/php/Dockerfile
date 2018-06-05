#  
# APACHE Dockerfile  
#  
# https://github.com/rzani/docker-workspace  
FROM rzani/php  
  
# File Author  
MAINTAINER Rodrigo Zani <rodrigo.zhs@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -yq default-jre wget  
  
RUN mkdir -p /opt/selenium && \  
wget --no-verbose http://selenium-
release.storage.googleapis.com/2.48/selenium-server-standalone-2.48.2.jar -O
/opt/selenium/selenium-server-standalone.jar  
  
RUN sudo useradd seluser --shell /bin/bash --create-home && \  
sudo usermod -a -G sudo seluser && \  
echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers && \  
echo 'seluser:secret' | chpasswd  
  
# Clean apt-get and other unusual things  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN rm -Rf /var/cache/* && \  
rm -Rf /usr/share/doc/* && \  
rm -Rf /usr/share/man/*  

