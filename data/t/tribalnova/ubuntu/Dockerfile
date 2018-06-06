FROM ubuntu:12.04.5  
MAINTAINER Nicolas Degardin <ndegardin@tribalnova.com>  
  
ENV PATH .:$PATH  
  
ENV DEBIAN_FRONTEND=noninteractive \  
TERM=xterm  
  
ARG APT=archive.ubuntu.com  
RUN sed "s@archive.ubuntu.com@$APT@" -i /etc/apt/sources.list  
RUN locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
LC_CTYPE=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8  
RUN apt-get clean && apt-get update && apt-get install -y util-linux apt-utils
ntp socat curl  
RUN ln -fs /usr/share/zoneinfo/GMT /etc/localtime  
  
# Prepare dev tools  
ADD files/configuration/zshrc /opt/docker/zshrc  
ADD files/install-devtools.sh /opt/docker/install-devtools.sh  
ADD files/startup-timezone.sh /opt/docker/startup-timezone.sh

