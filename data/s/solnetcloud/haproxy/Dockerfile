# HAProxy Dockerfile  
# Solnet Solutions  
# Version: 1.5.3 (1.5:1.5.3-1~ubuntu14.04.1)  
# Pull base image (Ubunu 14.04)  
FROM ubuntu:14.04  
# Build Instructions  
# When building use the following flags:  
# --tag "solnetcloud/haproxy:1.5.3"  
# Run Instructions:  
# You will want to expose the stats port (80) to the host  
# You will also want to expose the listen port of whatever you are load
balancing  
# Bind mount the haproxy configuration file read only from the host  
# When running use the following flags:  
# --restart=on-failure  
# -v <path_to_config_on_host>:/etc/haproxy/haproxy.cfg:ro  
# Information  
MAINTAINER Eric Duggan <eric.duggan@solnet.co.nz>  
LABEL Description="This image is used to stand up a HAProxy instance."
Version="1.5.3"  
  
# Patch notes:  
# Version 1.5.3  
# - Working container running HAProxy  
# Set the haproxy version to be pinned  
ENV HAP_PKG_VRS 1.5.3-1~ubuntu14.04.1  
# Install extra packages  
RUN \  
sed -i 's/^# \\(.*-backports\s\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y haproxy=1.5.3-1~ubuntu14.04.1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set timezone  
RUN \  
echo "Pacific/Auckland" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# Expose ports to other containers  
# Expose 8080: Stats page for HAProxy  
EXPOSE 8080  
# Define the default command as entrypoint  
ENTRYPOINT ["/usr/sbin/haproxy", "-f", "/etc/haproxy/haproxy.cfg"]  

