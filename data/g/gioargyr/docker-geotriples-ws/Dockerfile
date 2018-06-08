################################  
# Dockerfile for Geotriples WS #  
# BigDataEurope #  
# #  
# java 1.8.0_11 #  
# maven 3.0.5 #  
# git 1.9.1 #  
# tomcat 8.0.23 #  
################################  
FROM ubuntu:14.04  
MAINTAINER Giorgos Argyriou <gioargyr@gmail.com>  
  
ENV PORT 8080  
ENV TOMCAT_MAJOR_VERSION 8  
ENV TOMCAT_MINOR_VERSION 8.0.23  
# WGET INSTALLATION  
RUN apt-get update && apt-get install -y wget && apt-get clean  
  
# INSTALLATION JAVA SHELL VARIABLES  
ENV java_version 1.8.0_11  
ENV filename jdk-8u11-linux-x64.tar.gz  
ENV downloadlink http://download.oracle.com/otn-
pub/java/jdk/8u11-b12/$filename  
  
# DOWNLOAD JAVA AND ACCEPT LICENSE AGGREMENT  
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" -O /tmp/$filename $downloadlink  
  
# UNPACK JAVA  
RUN mkdir /opt/java-oracle && tar -zxf /tmp/$filename -C /opt/java-oracle/  
  
# CONFIGURE JAVA ENV VARIABLE  
ENV JAVA_HOME /opt/java-oracle/jdk$java_version  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# CONFIGURE SYMBOLIC LINKS FOR THE JAVA AND JAVAC EXECUTABLES  
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000
&& update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac
20000  
  
# INSTALL PREREQUISITIES  
RUN apt-get update && \  
apt-get install -y \  
maven \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# INSTALL TOMCAT  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \  
wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \  
tar zxf apache-tomcat-*.tar.gz && \  
rm apache-tomcat-*.tar.gz && \  
mv apache-tomcat* tomcat  
  
# DOWNLOAD AND BUILD  
RUN git clone https://github.com/big-data-europe/pilot-sc7-geotriples.git && \  
cd pilot-sc7-geotriples && \  
git checkout df72e83d50a9568d422bcd954db4652d9baf8e01 && \  
mvn package  
  
RUN mkdir /resources \  
&& cp /pilot-sc7-geotriples/target/*.war /tomcat/webapps  
  
ADD create_tomcat_admin_user.sh /create_tomcat_admin_user.sh  
ADD geotriples.sh /geotriples.sh  
ADD event-mapping.ttl /resources  
ADD change-mapping.ttl /resources  
ADD id.txt /resources  
  
RUN chmod +x /*.sh  
  
EXPOSE $PORT  
CMD ["/bin/bash", "/geotriples.sh"]  

