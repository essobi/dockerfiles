#start a tomcat-base image  
From centos:7  
MAINTAINER "lvqiang" <rainbow_free@126.com>  
ENV container docker  
  
#install  
RUN yum install -y vim-enhanced.x86_64  
RUN yum install -y wget  
  
#prepare environment  
ENV JAVA_HOME /usr/local/java  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin:$CATALINA_HOME/scripts  
  
#install java  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jdk/7u71-b14/jdk-7u71-linux-x64.tar.gz  
RUN tar -xvf jdk-7u71-linux-x64.tar.gz  
RUN rm jdk*.tar.gz  
RUN mv jdk* ${JAVA_HOME}  
  
#install tomcat  
RUN wget http://apache.opencas.org/tomcat/tomcat-7/v7.0.67/bin/apache-
tomcat-7.0.67.tar.gz  
Run tar -xvf apache-tomcat-7.0.67.tar.gz  
Run rm apache-tomcat*.tar.gz  
Run mv apache-tomcat* ${CATALINA_HOME}  
  
RUN groupadd tomcat  
RUN useradd -s /bin/bash -g tomcat tomcat  
RUN chown -Rf tomcat.tomcat /usr/local/tomcat  
  
#setting tomcat  
ADD settings.xml /usr/local/tomcat/conf/  
ADD tomcat-users.xml /usr/local/tomcat/conf/  
ADD server.xml /usr/local/tomcat/conf/  
  
# expose tomcat port  
EXPOSE 8080  
#run tomcat  
CMD ["catalina.sh", "run"]  

