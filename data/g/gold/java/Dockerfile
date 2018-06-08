#  
# Java 8 JRE  
#  
# Dockerfile Version 1.0.6  
# Oracle Java Runtime (JRE) version 1.8.0_66 64 bit  
#  
FROM debian:jessie  
  
MAINTAINER Alexander Holbreich (http://alexander.holbreich.org)  
  
# Install wget  
RUN apt-get update && apt-get install -y wget && apt-get clean  
  
#Some variables  
ENV java_version 1.8.0_66  
ENV filename jre-8u66-linux-x64.tar.gz  
#Download java  
ENV downloadlink http://download.oracle.com/otn-
pub/java/jdk/8u66-b17/$filename -O /tmp/$filename  
  
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" $downloadlink -O /tmp/$filename  
  
RUN mkdir /opt/java-oracle && tar -zxf /tmp/$filename -C /opt/java-oracle/  
  
#additional config  
ENV JAVA_HOME /opt/java-oracle/jre$java_version  
ENV PATH $JAVA_HOME/bin:$PATH  
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000  

