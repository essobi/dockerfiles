# debian jessie + oracle java  
#  
# VERSION 0.0.1  
#  
# 0.0.1 : initial creation of image with java version 1.8.0_72-b15 (766.4 MB)  
  
FROM debian:jessie  
  
MAINTAINER Robert Reihs <robert.reihs@gmail.com>  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get install -y oracle-java8-installer unzip \  
&& apt-get install -y oracle-java8-set-default  

