#  
# dockerfile - ubuntu 16.04, oracle-java8, mysql-server, maven  
#  
# Use ubuntu:16.04 as base image  
FROM ubuntu:16.04  
  
MAINTAINER Nimrod lahav <nimrod.lahav@gmail.com>  
  
# Install essentials  
RUN \  
apt-get update && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
rm -rf /var/lib/apt/lists/*  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Install MySql  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update && \  
apt-get install -y mysql-server mysql-client && \  
rm -rf /var/lib/apt/lists/*  
# Install maven  
RUN \  
apt-get update && \  
apt-get install -y maven && \  
rm -rf /var/lib/apt/lists/*  

