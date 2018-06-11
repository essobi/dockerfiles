FROM debian:8  
  
MAINTAINER Robert Frånlund <robert.franlund@poweruser.se>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Unifi and dependencies  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-get update && \  
apt-get -y install -t jessie-backports openjdk-8-jre-headless && \  
apt-get -y install wget mongodb-server jsvc binutils && \  
wget -O /tmp/unifi_sysvinit_all.deb \  
https://dl.ubnt.com/unifi/5.8.17-7f48eb2dea/unifi_sysvinit_all.deb && \  
dpkg --install /tmp/unifi_sysvinit_all.deb && \  
rm -rf /tmp/unifi_sysvinit_all.deb /var/lib/unifi/*  
# Expose ports  
EXPOSE 8080/tcp 8443/tcp 8880/tcp 8843/tcp 3478/udp  
  
# Add start script  
# 2016-10-25 - Fixed strange Docker Hub bug  
# https://forums.docker.com/t/automated-docker-build-fails/22831/27  
  
ADD assets /assets  
RUN mv /assets/start.sh / && rmdir /assets  
  
VOLUME ["/var/lib/unifi"]  
  
WORKDIR /var/lib/unifi  
  
CMD ["/start.sh"]  

