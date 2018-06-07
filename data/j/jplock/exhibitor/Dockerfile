# DOCKER-VERSION 1.1.2  
# VERSION 0.4  
FROM debian:jessie  
MAINTAINER Justin Plock <justin@plock.net>  
  
RUN apt-get update && apt-get install -y wget maven  
RUN wget -q -O /opt/pom.xml
https://raw.github.com/Netflix/exhibitor/master/exhibitor-
standalone/src/main/resources/buildscripts/standalone/maven/pom.xml  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
RUN cd /opt && mvn assembly:single  
  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/java", "-jar", "/opt/target/exhibitor-war-1.0-jar-with-
dependencies.jar"]  
CMD ["--help"]  

