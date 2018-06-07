# Optimized TexLive Installation, Layer reduction + Clean-up  
FROM ubuntu:16.04  
MAINTAINER Jonas Bernsdorff <jonas.bernsdorff@hpe.com>  
  
# Update packet lists  
RUN apt-get update &&\  
apt-get autoremove -y &&\  
apt-get install -fy make=4* \  
texlive-full \  
biber && \  
apt-get purge -y texlive*doc &&\  
apt-get clean &&\  
apt-get autoclean -y &&\  
rm -rf /tmp/* /var/tmp/* &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -f /etc/ssh/ssh_host_*  
  
# Create Volumes  
RUN mkdir /usr/share/fonts/external/ &&\  
mkdir /doc/  
  
VOLUME ["/doc/", "/usr/share/fonts/external/"]  
WORKDIR /doc  
CMD make  

