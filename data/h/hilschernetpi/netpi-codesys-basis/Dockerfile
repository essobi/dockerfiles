#use latest armv7hf compatible debian OS version from group resin.io as base
image  
FROM resin/armv7hf-debian:jessie  
  
#enable building ARM container on x86 machinery on the web (comment out next 3
lines if built on Raspberry)  
RUN [ "cross-build-start" ]  
  
#execute all commands as root  
USER root  
  
#labeling  
LABEL maintainer="netpi@hilscher.com" \  
version="V0.9.1.0" \  
description="Debian:jessie with SSH, user pi and CODESYS Control basis
settings"  
  
#version  
ENV HILSCHERNETPI_CODESYS_BASIS_VERSION 0.9.1.0  
#install ssh, create user "pi" and make him sudo  
RUN apt-get update \  
&& apt-get install -y openssh-server net-tools \  
&& mkdir /var/run/sshd \  
&& useradd --create-home --shell /bin/bash pi \  
&& echo 'pi:raspberry' | chpasswd \  
&& adduser pi sudo \  
&& touch /usr/bin/modprobe \  
&& chmod +x /usr/bin/modprobe \  
&& touch /etc/modules \  
&& apt-get -yqq autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
#do ports  
EXPOSE 22 1217  
#do entrypoint  
COPY "entrypoint.sh" /  
RUN chmod +x entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
#set STOPSGINAL  
STOPSIGNAL SIGTERM  
  
#stop processing ARM emulation (comment out next line if built on Raspberry)  
RUN [ "cross-build-end" ]  

