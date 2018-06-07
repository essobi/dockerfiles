# Base image  
FROM ubuntu:14.04  
  
# Update and then install necessary dependencies  
RUN apt-get update && \  
apt-get install -y software-properties-common python-software-properties
libgtk2.0-0  
  
# Add Sublime  
RUN add-apt-repository ppa:webupd8team/sublime-text-3 && \  
apt-get update && \  
apt-get install -y sublime-text-installer  
  
# Create the necessary dir used by Sublime  
RUN mkdir -p /usr/share/gvfs/remote-volume-monitors  
  
# Install python  
RUN apt-add-repository ppa:fkrull/deadsnakes-python2.7 && \  
apt-get update && \  
apt-get install -y python2.7 python2.7-dev  
  
# Need to install this in case package control is needed  
RUN locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales  
  
  
# Environment variables for package control  
ENV LANG=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
  
# I want to have the option of GIT  
RUN apt-get install -y git  
  
# Run  
CMD subl  

