# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to `latest`! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
FROM phusion/baseimage:0.9.8  
  
MAINTAINER tweakstreet <ci@tweakstreet.io>  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
################################  
# Repositories Init  
################################  
  
# RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >>
/etc/apt/sources.list  
RUN apt-get update && apt-get clean  
  
##################  
# Packages  
##################  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y \  
gawk \  
curl \  
wget  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
####################  
# Users  
####################  
  
# Add the tweakstreet user  
RUN useradd -m -d /home/tweakstreet tweakstreet  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  

