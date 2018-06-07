# Use phusion/baseimage as base image.  
FROM phusion/baseimage:0.9.18  
MAINTAINER Marcus Collier "dev@mjcollier.id.au"  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Install prerequisites  
RUN apt-get update; \  
apt-get install -y udhcpd  
  
# Set up start up scripts  
RUN mkdir /etc/service/udhcpd  
ADD udhcpd.sh /etc/service/udhcpd/run  
RUN chmod +x /etc/service/udhcpd/run  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose the port  
EXPOSE 67  
EXPOSE 67/udp  
EXPOSE 68  
EXPOSE 68/udp  
  
# Volumes  
VOLUME /data  

