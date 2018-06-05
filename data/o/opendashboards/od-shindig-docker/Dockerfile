##################################################################  
# OpenDashboards - Shindig - Docker - Bootstrap server  
#  
# Description  
# -----------  
# Creates a Docker image containing the latest stable version  
# of the Apache Shindig web app.  
#  
# Author: Chris Spiliotopoulos (@chefArchitect)  
##################################################################  
  
# Extend the official Jetty image  
FROM jetty:9.3.7  
  
MAINTAINER Chris Spiliotopoulos (@chefArchitect)  
  
# Download the latest stable version of the Apache Shindig web module from
Maven Central  
RUN wget http://central.maven.org/maven2/org/apache/shindig/shindig-
server/2.5.2/shindig-server-2.5.2.war -O ROOT.war  
  
# Unzip the .war package into the webapps Jetty directory  
RUN unzip ROOT.war -d webapps/ROOT  
  
#  
# Set some environment variables  
#  
  
# The default Shindig host - localhost  
ENV SHINDIG_HOST localhost  
  
# The default Shindig port - 8080  
ENV SHINDIG_PORT 8080  
  
#  
# Launch the Jetty engine  
#  
  
CMD java -Djava.io.tmpdir=/tmp/jetty -Dshindig.host=$SHINDIG_HOST
-Dshindig.port=$SHINDIG_PORT -jar /usr/local/jetty/start.jar
jetty.port=$SHINDIG_PORT  

