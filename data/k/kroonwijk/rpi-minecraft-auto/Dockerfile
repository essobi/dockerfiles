#
-----------------------------------------------------------------------------  
# rpi-minecraft  
#  
# Builds a Raspberry Pi (ARM) docker image that can run a Minecraft server  
# (http://minecraft.net/).  
#  
# Authors: Marco Kroonwijk  
# Updated: May 26, 2015  
# Require: Docker (http://www.docker.io/)  
#
-----------------------------------------------------------------------------  
# Base system is the Raspian ARM image from Resin  
FROM resin/rpi-raspbian  
  
  
# Make sure we don't get notifications we can't answer during building.  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Get system up to date to start with.  
RUN apt-get --yes update; apt-get --yes upgrade; apt-get --yes install
software-properties-common  
  
# The special trick here is to download and install the Oracle Java 8
installer from Launchpad.net  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get --yes update  
  
# Make sure the Oracle Java 8 license is pre-accepted, and install Java 8  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get --yes install curl oracle-java8-installer  
  
# Load in all of our config files.  
ADD ./scripts/start /start  
  
# Fix all permissions  
RUN chmod +x /start  
  
# 25565 is for minecraft  
EXPOSE 25565  
# /data contains static files and database  
VOLUME ["/data"]  
  
# /start runs it.  
CMD ["/start"]  

