FROM ubuntu:14.04  
MAINTAINER Jeyson Maia <jeyson@upspeck.io>  
  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
# Utilities  
RUN apt-get update && apt-get -y install software-properties-common unzip  
  
# Install Java.  
RUN apt-get update \  
&& apt-get install -y wget openssl ca-certificates \  
&& cd /tmp \  
&& wget -qO jdk7.tar.gz \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz
\  
&& tar xzf jdk7.tar.gz -C /opt \  
&& mv /opt/jdk* /opt/java \  
&& rm /tmp/jdk7.tar.gz \  
&& update-alternatives \--install /usr/bin/java java /opt/java/bin/java 100 \  
&& update-alternatives \--install /usr/bin/javac javac /opt/java/bin/javac 100  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /opt/java  

