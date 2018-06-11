##################################################  
#  
# Dockerfile for Base Image  
# (Ubuntu 16.04 with Dnsmasq and common utilities)  
#  
###################################################  
  
FROM ubuntu:16.04  
MAINTAINER Unisis <contacto@unisis.com.ar>  
  
# To allow the use of nano  
ENV TERM=xterm  
  
# Update packages  
ENV PACKAGES_REFRESHED_AT 2016-04-29  
RUN apt-get update  
  
# Install packages  
RUN apt-get install -y --no-install-recommends \  
git \  
zip \  
wget \  
curl \  
nano \  
s3cmd \  
rsync \  
unzip \  
dnsmasq  
  
# DnsMasq configuration  
ENV HOSTS_FILE /etc/dnsmasq.d/0hosts  
ADD config/dnsmasq.conf /etc/dnsmasq.conf  
ADD config/resolv.dnsmasq.conf /etc/resolv.dnsmasq.conf  
  
# Add script to configure hosts  
ADD scripts/set-host /usr/sbin/set-host  
RUN chmod +x /usr/sbin/set-host  
  
# Add script to list hosts  
ADD scripts/list-hosts /usr/sbin/list-hosts  
RUN chmod +x /usr/sbin/list-hosts  
  
# Start command  
CMD ["/bin/bash"]  

