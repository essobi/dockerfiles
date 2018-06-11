FROM phusion/baseimage:0.9.19  
MAINTAINER Giorgio Aresu <giorgioaresu@gmail.com>  
  
ENV BRANCH master  
  
WORKDIR /tmp  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
CMD ["/sbin/my_init"]  
  
RUN \  
# Update base image  
apt-get update && \  
apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
# Update and install packages  
apt-get update && \  
apt-get install -y \  
git \  
sudo \  
wget \  
&& \  
  
# Cleanup  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD build-zm.sh /usr/local/bin/build-zm.sh  
RUN chmod +x /usr/local/bin/build-zm.sh  
  
CMD build-zm.sh

