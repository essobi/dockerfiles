# Base Image Debian with Java  
FROM debian:7.6  
MAINTAINER Stephan Harbauer "docker@harbauer.org"  
# Install generall things first  
RUN apt-get update  
RUN noninteractive=noninteractive apt-get install ca-certificates -y  
  
# Add java repo  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" |
tee -a /etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise
main" | tee -a /etc/apt/sources.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
  
RUN apt-get update  
  
# Install Java 7  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN noninteractive=noninteractive apt-get install oracle-java7-installer ca-
certificates -y

