# Spoke Dockerfile for dns  
FROM radial/spoke-base:latest  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update && apt-get -qyV install \  
dnsmasq &&\  
apt-get clean  
  
# Set Spoke ID  
ENV SPOKE_NAME dns  
  
COPY /entrypoint.sh /entrypoint.sh  
  
EXPOSE 53  
EXPOSE 53/udp  

