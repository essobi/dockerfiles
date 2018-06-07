FROM phusion/baseimage:0.9.16  
MAINTAINER Harsh Vakharia <harshjv@gmail.com>  
  
# Default baseimage settings  
ENV HOME /root  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
CMD ["/sbin/my_init"]  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update software list, install nodejs, npm & clear cache  
RUN apt-get update && \  
apt-get install -y nodejs npm && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
# Install gruntjs & clear cache  
RUN npm install -g grunt-cli && \  
rm -rf ~/.npm && \  
npm cache clear  
  
# Configure nodejs  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Add gruntjs volume  
VOLUME ["/var/gruntjs"]  
  
# Set WORKDIR  
WORKDIR /var/gruntjs  
  
# Set grunt as default command  
CMD grunt  

