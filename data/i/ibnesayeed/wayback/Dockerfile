FROM tomcat:7-jre8  
MAINTAINER Sawood Alam <ibnesayeed@gmail.com>  
  
RUN rm -rf /usr/local/tomcat/webapps/*  
ADD ROOT /usr/local/tomcat/webapps/ROOT  
  
VOLUME ["/wayback/warcs"]  
  
ENV WAYBACK_URL_SCHEME http  
ENV WAYBACK_URL_HOST localhost  
ENV WAYBACK_URL_PORT 8080  
ENV WAYBACK_URL_PREFIX http://localhost:8080  

