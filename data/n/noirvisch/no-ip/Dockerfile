# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.15  
MAINTAINER noirvisch <info@noirvisch.com>  
  
# Set correct environment variables.  
ENV HOME /root  
  
  
# disable ssh service  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Do it this way to avoid creating a useless 100+ MB layer for the user to
download  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y make gcc && \  
\  
cd /root && \  
curl -o noip-duc-linux.tar.gz http://www.noip.com/client/linux/noip-duc-
linux.tar.gz && \  
tar -xzf noip-duc-linux.tar.gz --wildcards 'noip*' && \  
\  
cd /root/noip-*/ && \  
make && \  
mv noip2 /root && \  
cd /root && \  
rm -rf /root/noip-* && \  
\  
apt-get remove -y make gcc && \  
apt-get autoremove -y && \  
apt-get autoclean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup the service  
RUN mkdir /etc/service/noip/ && mkdir -p /data/no-ip/  
ADD docker_noip.sh /etc/service/noip/run  
RUN chmod +x /etc/service/noip/run  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

