FROM debian:8  
MAINTAINER Raphael Noailles <docker@noailles.de>  
  
# Set correct environment variables  
ENV HOME /root  
  
# don't ask for stupid things  
env DEBIAN_FRONTEND noninteractive  
RUN echo APT::Install-Recommends "0"; >> /etc/apt/apt.conf  
RUN echo APT::Install-Suggests "0"; >> /etc/apt/apt.conf  
  
# update the system  
RUN echo "deb http://ftp.de.debian.org/debian/ jessie-backports main contrib
non-free" > /etc/apt/sources.list.d/backports.list  
RUN apt-get -y update && apt-get -y upgrade && dpkg-divert --local \--rename
--add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl  
  
# Install Tools  
RUN apt-get install -y wget curl locales locales-all unzip sudo  
  
# Configure timezone and locale  
RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure tzdata  
#RUN export LANGUAGE=en_US.UTF-8 && \  
# export LANG=en_US.UTF-8 && \  
# export LC_ALL=en_US.UTF-8 && \  
# locale-gen en_US.UTF-8 && \  
# dpkg-reconfigure locales  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

