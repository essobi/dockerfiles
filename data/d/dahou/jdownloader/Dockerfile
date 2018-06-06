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
  
# add repositories for jdownloader and java  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list  
RUN echo "deb http://ppa.launchpad.net/jd-team/jdownloader/ubuntu trusty main"
| tee -a /etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/jd-team/jdownloader/ubuntu trusty
main" | tee -a /etc/apt/sources.list  
  
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6A68F637  
  
# Install packages  
RUN sudo apt-get update -qq  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo
debconf-set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-
set-selections  
RUN sudo apt-get install -qy --force-yes oracle-java8-installer jdownloader-
installer  
  
VOLUME /config  
VOLUME /unraid_media  
  
# Cleanup  
RUN apt-get clean -y  
RUN rm -rf /var/lib/apt/lists/* /var/cache/* /var/tmp/*  
  

