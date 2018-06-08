FROM ubuntu:14.04.2  
MAINTAINER Richard Attermeyer "richard.attermeyer@gmail.com"  
ENV REFRESHED_AT 2015-07-28  
LABEL JAVA_MAJOR_VERSION=8 JAVA_VERSION=8u45  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# update und install software-properties-common (ubuntu >= 12.10) to be able
to use add-apt-repository  
RUN apt-get -qq update && apt-get -qq -y install software-properties-common &&
apt-get -qq upgrade  
  
# add PPA for java and resynchronize package index files from their sources
and install openjdk-8-jdk  
RUN add-apt-repository ppa:openjdk-r/ppa && apt-get -qq update && apt-get -qq
-y install openjdk-8-jdk=8u45-b14-1~14.04  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

