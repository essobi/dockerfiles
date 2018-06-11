#  
# Activiti Dockerfile  
#  
FROM tomcat:9-jre8-alpine  
MAINTAINER Philippe Warnon "warnon.philippe@gmail.com"  
EXPOSE 8080  
# Activiti  
ADD activiti/* /usr/local/tomcat/webapps/  
  
# MySQL  
ADD mysql/* /usr/local/tomcat/lib/  
  
# PostgreSQL  
ADD postgres/* /usr/local/tomcat/lib/  
  
# Configure  
ADD assets /assets  
RUN cp /assets/config/tomcat/tomcat-users.xml /usr/local/tomcat/conf  
#RUN cp -f /assets/config/explorer/engine.properties
/usr/local/tomcat/webapps/activiti-app/WEB-INF/classes  
CMD ["/bin/bash", "/assets/init"]  

