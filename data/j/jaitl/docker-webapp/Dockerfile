FROM ubuntu:14.04  
MAINTAINER Jaitl  
  
RUN apt-get update  
RUN apt-get -yq install openjdk-7-jre wget  
  
ENV VERSION 8.0.12  
RUN wget -q http://apache-
mirror.rbc.ru/pub/apache/tomcat/tomcat-8/v${VERSION}/bin/apache-
tomcat-${VERSION}.tar.gz  
RUN tar zxf apache-tomcat-${VERSION}.tar.gz  
RUN rm apache-tomcat-${VERSION}.tar.gz  
  
RUN mv apache-tomcat-${VERSION} tomcat8  
RUN mv tomcat8 /opt  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
ADD sample.war /opt/tomcat8/webapps/sample.war  
  
EXPOSE 8080  
CMD ["/run.sh"]

