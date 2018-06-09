# DOCKER-VERSION 1.2.0  
FROM centos  
MAINTAINER Manuel DEQUEKER, manuel.dequeker@webexpenses.com  
  
#Install WGET  
RUN yum install -y wget  
  
#Install tar  
RUN yum install -y tar  
  
# Download JDK  
RUN yum install -y java-1.7.0-openjdk  
  
# Download Apache Tomcat 7  
RUN cd /tmp;wget
http://archive.apache.org/dist/tomcat/tomcat-7/v7.0.55/bin/apache-
tomcat-7.0.55.tar.gz  
  
# untar and move to proper location  
RUN cd /tmp;gunzip apache-tomcat-7.0.55.tar.gz  
RUN cd /tmp;tar xvf apache-tomcat-7.0.55.tar  
RUN cd /tmp;mv apache-tomcat-7.0.55 /opt/tomcat7  
RUN chmod -R 755 /opt/tomcat7  
  
RUN rm -rf /opt/tomcat7/webapps/*  
ADD sample.war /opt/tomcat7/webapps/  
ADD testweb.war /opt/tomcat7/webapps/  
  
EXPOSE 8080  
CMD /opt/tomcat7/bin/catalina.sh run

