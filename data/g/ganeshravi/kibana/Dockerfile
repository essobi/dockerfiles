FROM dockerfile/java:oracle-java7  
MAINTAINER Ganesh Ravi <ganesh.reddy.22@gmail.com>  
  
ENV TOMCAT_MAJOR_VERSION 8  
ENV TOMCAT_MINOR_VERSION 8.0.15  
# INSTALL TOMCAT  
RUN wget
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz  
RUN wget -O-
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_MINOR_VERSION}/bin/apache-
tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c -  
RUN tar zxf apache-tomcat-*.tar.gz  
RUN mv apache-tomcat*/ /tomcat/  
RUN rm -f /apache-tomcat-*.tar.gz  
  
ENV CATALINA_HOME /tomcat  
  
ADD create_tomcat_user.sh /usr/local/bin/create_tomcat_user.sh  
RUN chmod +x /usr/local/bin/create_tomcat_user.sh  
  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
ENV KIBANA_VERSION 3.1.2  
# INSTALL KIBANA  
RUN wget
https://download.elasticsearch.org/kibana/kibana/kibana-${KIBANA_VERSION}.tar.gz  
RUN tar zxf kibana-*.tar.gz  
RUN mv kibana-*/ /tomcat/webapps/ROOT/kibana/  
RUN rm -f /kibana-*.tar.gz  
  
EXPOSE 8080  
CMD ["/bin/bash", "/usr/local/bin/run.sh"]  

