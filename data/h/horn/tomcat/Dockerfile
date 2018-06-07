# Based on Feng Honglin <hfeng@tutum.co> container called tutum/tomcat7  
# https://github.com/tutumcloud/tutum-docker-tomcat  
# It is just based on Docker's base Ubuntu with a minimal JRE  
FROM ubuntu:trusty  
  
MAINTAINER David Weber <dave@veryflatcat.com>  
  
# Helper to add deb file source  
RUN apt-get update -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-7-jre-headless  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget pwgen  
  
ENV TOMCAT_VERSION 8.0.9  
ENV CATALINA_HOME /tomcat  
  
# INSTALL TOMCAT  
RUN wget
http://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz  
RUN wget -O-
https://www.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz.md5 | md5sum -c -  
RUN tar zxf apache-tomcat-*.tar.gz && rm apache-tomcat-*.tar.gz && mv apache-
tomcat* tomcat  
  
ADD create_tomcat_admin_user.sh /create_tomcat_admin_user.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
EXPOSE 8080  
CMD ["/run.sh"]

