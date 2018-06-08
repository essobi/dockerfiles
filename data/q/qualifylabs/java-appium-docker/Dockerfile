FROM ubuntu:14.04  
  
MAINTAINER Mehmet Bora Ezer <bora@qualifylabs.com>  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PATH $JAVA_HOME/bin:$PATH  
  
RUN \  
apt-get -y install maven zip && \  
apt-get clean autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
RUN mkdir /java  
VOLUME /java  
WORKDIR /java

