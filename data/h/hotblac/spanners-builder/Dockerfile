FROM maven:3.3.3-jdk-8  
MAINTAINER Stuart 'Stevie' Leitch <hotblack@disasterarea.org.uk>  
  
# Copy settings.xml  
ADD settings.xml $MAVEN_HOME/conf/settings.xml  
  
# Build and deploy to the spanners-webserver container  
CMD ["mvn", "clean", "install", "tomcat7:redeploy", "-Pdockerbuild"]  
  

