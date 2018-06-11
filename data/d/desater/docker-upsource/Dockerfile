#######################################################################  
# Dockerfile to build an Ubuntu Oracle Java SDK container image  
# Based on Ubuntu  
#######################################################################  
  
# Set the base image to Ubuntu  
FROM oreomitch/ubuntu-jdk:15.04-JDK8  
# File Author / Maintainer  
MAINTAINER Mitchell Wong Ho <oreomitch@gmail.com>  
  
USER root  
ENV JAVA_HOME /usr/bin/java  
RUN apt-get update  
RUN apt-get install -y unzip zip  
  
  
ENV UPSOURCE_VERSION 3.0.4346  
  
  
VOLUME
["/opt/Upsource/conf","/opt/Upsource/data","/opt/Upsource/logs","/opt/Upsource/backups"]  
WORKDIR /opt  
  
RUN mkdir -p /home/upsource \  
&& groupadd -g 999 upsource \  
&& useradd -u 999 -g upsource -d /home/upsource upsource \  
&& chown -R upsource:upsource /home/upsource  
  
ADD https://download.jetbrains.com/upsource/upsource-$UPSOURCE_VERSION.zip
/opt/  
  
RUN unzip upsource-$UPSOURCE_VERSION.zip \  
&& rm -rf upsource-$UPSOURCE_VERSION.zip \  
&& chown -R upsource:upsource Upsource  
  
USER upsource  
EXPOSE 8080  
WORKDIR /opt/Upsource  
  
CMD ["bin/upsource.sh", "run"]  

