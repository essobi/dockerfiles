FROM maven:3.5-jdk-8  
MAINTAINER dev@taverna.incubator.apache.org  
  
  
# Update below according to  
# https://taverna.incubator.apache.org/download/server/  
ENV TAVSERV_VERSION 3.1.0-incubating  
ENV TAVSERV_KEYS https://www.apache.org/dist/incubator/taverna/KEYS  
  
WORKDIR /tmp  
  
RUN wget $TAVSERV_KEYS && gpg --import KEYS  
RUN mvn -B dependency:copy -DoutputDirectory=/tmp
-Dartifact=org.apache.taverna.server:taverna-server-
webapp:$TAVSERV_VERSION:war  
RUN mvn -B dependency:copy -DoutputDirectory=/tmp
-Dartifact=org.apache.taverna.server:taverna-server-
webapp:$TAVSERV_VERSION:war.asc  
RUN gpg --verify *.asc  
RUN mv *.war /taverna-server.war  
  
# Second stage, Tomcat container  
FROM tomcat:8-jre8  
  
# Install "time"  
RUN apt-get update && apt-get install -qqy time && apt-get clean  
  
# (assume WORKDIR is in tomcat dir)  
# Clear default apps  
RUN rm -rf webapps/*  
  
# Get WAR from previous stage, deploy at ROOT  
COPY \--from=0 /taverna-server.war /tmp/taverna-server.war  
  
# Manual unpack of WAR to customize properties  
RUN rm -rf webapps/* && \  
mkdir webapps/ROOT && cd webapps/ROOT && \  
unzip /tmp/taverna-server.war  
  
# Set up unsecured connections, server defaults and users.  
ADD web.xml tavernaserver.properties webapps/ROOT/WEB-INF/  
ADD users.properties webapps/ROOT/WEB-INF/security/  
  
# Expose both http and ajp  
EXPOSE 8080  
EXPOSE 8009  
# Expose the Taverna Server working directory for debugging.  
VOLUME ["/tmp"]  

