#use latest armv7hf compatible raspbian OS version from group resin.io as base
image  
FROM resin/armv7hf-debian:jessie  
  
#enable building ARM container on x86 machinery on the web (comment out next
line if built on Raspberry)  
RUN [ "cross-build-start" ]  
  
#labeling  
LABEL maintainer="netpi@hilscher.com" \  
version="V1.1.0.1" \  
description="Containerized Docker and Git for netPI onboard container
developments"  
  
#version  
ENV HILSCHERNETPI_CONTAINER_BUILD_ENVIRONMENT 0.9.1.0  
#copy files  
COPY "./init.d/*" /etc/init.d/  
  
#do installation  
RUN apt-get update \  
&& apt-get install -y git openssh-server \  
#do users  
&& echo 'root:root' | chpasswd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& mkdir /var/run/sshd \  
#install docker  
&& curl -sSL https://get.docker.com | sh \  
#clean up  
&& apt-get -yqq autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
#set the entrypoint  
ENTRYPOINT ["/etc/init.d/entrypoint.sh"]  
  
#SSH Port  
EXPOSE 22  
#set stop signal  
STOPSIGNAL SIGTERM  
  
#stop processing ARM emulation (comment out next line if built on Raspberry)  
RUN [ "cross-build-end" ]  

