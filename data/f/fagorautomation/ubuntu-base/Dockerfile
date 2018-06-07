# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to `latest`! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
FROM phusion/baseimage:0.10.1  
# Set correct environment variables.  
ENV HOME /root  
  
# Update OS.  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
RUN apt-get update  
  
# upgrade  
# RUN apt-get -y upgrade  
# Install basic packages.  
RUN apt-get install -y curl git htop unzip vim wget byobu make  
  
# use bash instead of dash  
RUN echo "dash dash/sh boolean false" | debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash  
  
CMD ["/sbin/my_init"]  
  

