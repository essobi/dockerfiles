FROM debian  
MAINTAINER Steven Pritchard <steven.pritchard@gmail.com>  
  
COPY ["unifi-entrypoint", "/usr/local/sbin/unifi-entrypoint"]  
RUN apt update && \  
apt upgrade -y && \  
apt install -y gnupg && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
COPY ["unifi.list", "/etc/apt/sources.list.d/unifi.list"]  
RUN apt update && \  
apt upgrade -y && \  
apt install -y unifi pcregrep && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/var/lib/unifi", "/var/log/unifi", "/var/run/unifi"]  
  
ENTRYPOINT ["/usr/local/sbin/unifi-entrypoint"]  
  
# https://help.ubnt.com/hc/en-us/articles/204910084-UniFi-Change-Default-
Ports-for-Controller-and-UAPs  
EXPOSE 8080 8443 8880 8843 3478/udp  

