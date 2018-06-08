FROM ubuntu:14.04  
MAINTAINER RAVI A <ravi@bizruntime.com>  
RUN apt-get update && apt-get install -y tomcat7  
ADD webapp.war /var/lib/tomcat7/webapps/  
CMD export CATALINA_BASE=/var/lib/tomcat7 &&
/usr/share/tomcat7/bin/catalina.sh run  

