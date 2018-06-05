############################################################  
# Dockerfile for pxe-server serving ubuntu netboot  
# Based on alpine  
############################################################  
FROM alpine  
MAINTAINER Runar Klemetsdal  
ADD http://archive.ubuntu.com/ubuntu/dists/trusty-updates/main/installer-
amd64/current/images/netboot/netboot.tar.gz /netboot.tar.gz  
RUN apk update && \  
apk add dnsmasq && \  
apk add tar && \  
mkdir /tftpboot && \  
tar -C /tftpboot -xvf /netboot.tar.gz && \  
chown -R nobody:nogroup /tftpboot  
COPY dnsmasq.conf /etc/dnsmasq.conf  
EXPOSE 69/udp  
ENTRYPOINT ["/usr/sbin/dnsmasq", "-k"]  

