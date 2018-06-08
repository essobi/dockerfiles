FROM ubuntu:14.04  
MAINTAINER Ryan Ratcliff <ryan@ryanratcliff.net>  
ENV refreshed_at 2014-11-26  
  
RUN apt-get -yqq update  
RUN apt-get -yqq install software-properties-common python-software-properties  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
RUN mkdir -p /app  
  
# Define working directory.  
WORKDIR /app  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

