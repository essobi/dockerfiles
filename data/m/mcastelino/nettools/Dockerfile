# Dockerfile to build a ubuntu container with common  
# networking tools  
# Set the base image to Ubuntu  
FROM ubuntu  
  
# File Author / Maintainer  
MAINTAINER manohar.r.castelino@intel.com  
  
# Update the repository sources list  
RUN apt-get update  
  
# Install common tools  
RUN apt-get install -y dnsutils curl inetutils-traceroute iputils-ping net-
tools iproute mtr-tiny netcat ethtool  
RUN apt-get install -y iperf  

