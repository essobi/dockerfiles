FROM tomcat:alpine  
  
MAINTAINER Blueur  
  
ARG TOMCAT_USER  
ENV TOMCAT_USER ${TOMCAT_USER:-tomcat}  
  
ARG TOMCAT_PASSWORD  
ENV TOMCAT_PASSWORD ${TOMCAT_PASSWORD:-tomcat}  
  
CMD echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?><tomcat-users><role
rolename=\"admin-gui\"/><role rolename=\"manager-gui\"/><user
username=\"${TOMCAT_USER}\" password=\"${TOMCAT_PASSWORD}\" roles=\"admin-
gui,manager-gui\"/></tomcat-users>" > conf/tomcat-users.xml \  
&& catalina.sh run

