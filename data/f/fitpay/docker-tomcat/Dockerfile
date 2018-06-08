FROM centos:7  
MAINTAINER Scott Stevelinck <scott@fit-pay.com>  
  
RUN yum update -y && yum clean all  
RUN yum install epel-release -y  
RUN yum install wget pwgen java-1.8.0-openjdk -y  
  
ENV TOMCAT_MAJOR_VERSION 7  
ENV TOMCAT_MINOR_VERSION 7.0.65  
ENV CATALINA_HOME /tomcat  
  
RUN wget -q
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \  
wget -qO-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \  
tar zxf apache-tomcat-*.tar.gz && \  
rm apache-tomcat-*.tar.gz && \  
mv apache-tomcat* tomcat  
RUN rm -rf /tomcat/webapps/*  
  
ADD server-ssl.xml /tomcat/conf/server-ssl.xml  
ADD server-default.xml /tomcat/conf/server-default.xml  
RUN rm -rf /tomcat/conf/server.xml  
  
ADD create_tomcat_admin_user.sh /create_tomcat_admin_user.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
CMD ["/run.sh"]  

