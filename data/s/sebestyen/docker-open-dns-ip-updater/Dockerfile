# A minimal Ubuntu base image modified for Docker-friendliness  
# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.18  
MAINTAINER Roberto Sebestyen <roberto@sebestyen.ca>  
  
VOLUME ["/config"]  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Prepare apt-get to make sure we have latest sources  
RUN apt-get update  
  
# To install packages for ssl communication in perl. This is required for
authentication.  
RUN apt-get -y install libio-socket-ssl-perl  
  
# Lets install ddclient application that we will use to do dynamic IP updates  
RUN apt-get -y install ddclient  
  
# Create template config file  
ADD ddclient.conf /root/ddclient/ddclient.conf  
  
# Add our phusion/baseimage init scripts for ddclient  
# All scripts must exit correctly, e.g. with exit code 0. If any script exits
with a non-zero exit code, the booting will fail.  
RUN mkdir -p /etc/my_init.d  
ADD ddclient-init.sh /etc/my_init.d/ddclient-init.sh  
RUN chmod +x /etc/my_init.d/ddclient-init.sh  
  
# Add our phusion/baseimage daemon, https://github.com/phusion/baseimage-
docker#adding_additional_daemons  
RUN mkdir /etc/service/ddclient  
ADD ddclient.sh /etc/service/ddclient/run  
RUN chmod +x /etc/service/ddclient/run  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

