# Dockerfile for the Radial distro base.  
#  
# This image is a base for the 'radial/distro' images containing items that
are  
# common to all the regional builds.  
FROM ubuntu:14.04  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Enable multiverse  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
  
# Insert bashrc  
ADD bashrc /root/.bashrc  
  
# Set HOME so bashrc is sourced  
ENV HOME /root  
  
# Set locale  
# Note: preseeding debconf is 'better', but didn't want to install  
# 'debconf-utils' just to do this in more steps.  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

