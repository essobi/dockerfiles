FROM tomcat:7-jre8  
MAINTAINER Stuart 'Stevie' Leitch <hotblack@disasterarea.org.uk>  
  
# context.xml contains jndi connection to spanners-database  
ADD tomcat/context.xml $CATALINA_HOME/conf/  
  
# tomcat-users.xml sets up user accounts for the Tomcat manager GUI  
# and script access for Maven deployments  
ADD tomcat/tomcat-users.xml $CATALINA_HOME/conf/  
  
# MySQL driver jar  
ADD tomcat/mysql-connector-java-5.1.36-bin.jar $CATALINA_HOME/lib/  
  
# Install spanners-mvc war from Maven repo  
RUN wget http://www.disasterarea.co.uk/maven/org/dontpanic/spanners-
mvc/3.5/spanners-mvc-3.5.war -O /usr/local/tomcat/webapps/spanners-mvc.war  
  

