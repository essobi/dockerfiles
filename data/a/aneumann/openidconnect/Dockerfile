FROM learninglayers/tomcat:8.5.9  
MAINTAINER Petru Nicolaescu  
  
  
RUN apt-get update && apt-get install -y \  
mysql-client  
# Add the war from Jenkins  
ADD http://layers.dbis.rwth-
aachen.de/jenkins/job/OpenIDConnect%20Server/lastSuccessfulBuild/artifact/openidconnectldapoverlay/ldap-
server-overlay/target/o%23oauth2.war ${TOMCAT_HOME}/webapps/o#oauth2.war  

