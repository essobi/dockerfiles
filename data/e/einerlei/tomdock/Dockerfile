######################################################  
## DOCK DOCK DOCK DOCK TOM !!  
######################################################  
  
FROM tomcat:8.0.20-jre8  
MAINTAINER "einerlei"  
  
RUN mkdir /usr/local/tomcat/webapps/myapp  
COPY tomcat-users.xml /usr/local/tomcat/conf/  
COPY sample.war /usr/local/tomcat/webapps/  
  
RUN /usr/local/tomcat/bin/catalina.sh start &  
  

