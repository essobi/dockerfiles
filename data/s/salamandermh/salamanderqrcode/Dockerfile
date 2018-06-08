FROM tomcat:8.5.24-jre8-alpine  
  
MAINTAINER salamander  
  
RUN rm -rf /usr/local/tomcat/webapps/ROOT  
COPY ./qrcode.war /usr/local/tomcat/webapps/ROOT.war  
COPY ./server.xml /usr/local/tomcat/conf

