FROM ubuntu:17.10  
MAINTAINER RazzDazz  
# Using instructions from  
# https://help.ubnt.com/hc/en-us/articles/220066768-UniFi-How-to-Install-
Update-via-APT-on-Debian-or-Ubuntu  
  
ENV REFRESHED_AT 2018-04-02  
ENV DEBIAN_FRONTEND noninteractive  
# Controller Version 5.7.20  
# Ports used by unfi controller  
# https://help.ubnt.com/hc/en-us/articles/218506997-UniFi-Ports-Used  
# port for UAP to inform controller unifi.http.port=8080  
# EXPOSE 8080/tcp  
# port for controller GUI / API, as seen in web browser unifi.https.port=8443  
# EXPOSE 8443/tcp  
# port for HTTP portal redirect portal.http.port=8880  
# EXPOSE 8880/tcp  
# port for HTTPS portal redirect portal.https.port=8843  
# EXPOSE 8843/tcp  
# port used for throughput measurement, including UniFi mobile speedtest
unifi.throughput.port=6789  
# EXPOSE 6789/tcp  
# local-bound port for DB server unifi.db.port=27117  
# EXPOSE 27117  
# UDP port used for STUN. v4.5.2+ unifi.stun.port=3478  
# EXPOSE 3478/udp  
# port 8881 for redirector port for wireless clients (reserved for for device
redirector.  
# No need to open firewall on controller, but avoid using these ports (v3.2.9+
and v4.6.0+))  
# EXPOSE 8881  
# port 8882 for redirector port for wired clients (reserved for for device
redirector.  
# No need to open firewall on controller, but avoid using these ports (v3.2.9+
and v4.6.0+))  
# EXPOSE 8882  
# UDP ports 5656-5699 for AP-EDU Broadcasts  
# EXPOSE 5656-5699  
  
EXPOSE 8080/tcp 8443/tcp 8880/tcp 8843/tcp 6789/tcp 3478/udp  
  
# Update packages to install java  
RUN apt-get -yqq update && \  
apt-get -yqq upgrade && \  
apt-get --no-install-recommends -yqq install openjdk-8-jre-headless && \  
rm -rf /var/lib/apt/lists/*  
# Update packages to install dirmngr needed by apt-key and get GPG keys for
Ubiquiti  
RUN apt-get -yqq update && \  
apt-get -yqq upgrade && \  
apt-get --no-install-recommends -yqq install dirmngr && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50 && \  
rm -rf /var/lib/apt/lists/*  
# Add sources for Ubiquiti  
RUN echo "deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti" >
/etc/apt/sources.list.d/ubiquiti.list  
  
# Update packages for installation of unifi controller  
RUN apt-get update -yqq && \  
apt-get upgrade -yqq && \  
apt-get --no-install-recommends -yqq install unifi && \  
rm -rf /var/lib/apt/lists/*  
# Publishing directories  
VOLUME /usr/lib/unifi/data  
VOLUME /usr/lib/unifi/logs  
# Set workdir  
WORKDIR /usr/lib/unifi  
# Run unifi-controller via docker exec:  
# run directly java command and do not use shell  
# this allows clean docker stop (send sigterm to process with pid 1)  
# further reading: https://www.ctl.io/developers/blog/post/gracefully-
stopping-docker-containers  
CMD ["java","-jar","/usr/lib/unifi/lib/ace.jar","start"]  

