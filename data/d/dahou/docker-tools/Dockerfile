FROM phusion/baseimage:0.9.15  
#FROM ubuntu:14.04  
MAINTAINER dahou  
#Based on the work of needo  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
# Thank you smdion  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
RUN usermod -d /config nobody  
  
# chfn workaround - Known issue within Dockers  
RUN ln -s -f /bin/true /usr/bin/chfn  
  
# Install packages  
RUN apt-get update -qq  
RUN apt-get install -qq --force-yes openjdk-7-jre wget  
  
# Install filebot  
RUN wget -O filebot-amd64.deb
'http://filebot.sourceforge.net/download.php?type=deb&arch=amd64'  
RUN dpkg --force-depends -i filebot-*.deb && rm filebot-*.deb  
  
# make config.yml and hardlink to /config  
RUN ln -s /root/.flexget /config  
  
VOLUME /config  
  
# Cleanup  
RUN apt-get clean -y  
RUN rm -rf /var/lib/apt/lists/* /var/cache/* /var/tmp/*  
  

