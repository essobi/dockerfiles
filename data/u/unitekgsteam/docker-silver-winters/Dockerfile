#
------------------------------------------------------------------------------  
# Docker provisioning script for the docker-laravel web server stack  
#  
# e.g. docker build -t mtmacdonald/docker-laravel:version .  
#
------------------------------------------------------------------------------  
#
------------------------------------------------------------------------------  
# Start with the official Ubuntu 14.04 base image  
#
------------------------------------------------------------------------------  
FROM ubuntu:14.04  
MAINTAINER Steve Yardumian  
  
# Set correct environment variables  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use Supervisor to run and manage all other services  
CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord.conf"]  
  
#
------------------------------------------------------------------------------  
# Provision the server  
#
------------------------------------------------------------------------------  
#PATCHED for when mounting a Mac OS X folder in VBox  
RUN usermod -u 1000 www-data  
  
RUN mkdir /provision  
ADD provision /provision  
RUN /provision/provision.sh  
  
#
------------------------------------------------------------------------------  
# Prepare image for use  
#
------------------------------------------------------------------------------  
# Expose ports  
EXPOSE 22 80 443  
#
------------------------------------------------------------------------------  
# Set locale (support UTF-8 in the container terminal)  
#
------------------------------------------------------------------------------  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
#
------------------------------------------------------------------------------  
# Clean up  
#
------------------------------------------------------------------------------  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

