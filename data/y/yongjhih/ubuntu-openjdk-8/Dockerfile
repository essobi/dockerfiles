FROM ubuntu  
  
MAINTAINER Andrew Chen <yongjhih@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y wget git curl zip software-
properties-common && \  
add-apt-repository ppa:openjdk-r/ppa && \  
apt-get update && apt-get install -y openjdk-7-jdk openjdk-8-jdk && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JAVA7_HOME /usr/lib/jvm/java-7-openjdk-amd64  
ENV JAVA8_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV JAVA_HOME $JAVA8_HOME  
ENV JAVA_TOOL_OPTIONS "-Dfile.encoding=UTF8"  

