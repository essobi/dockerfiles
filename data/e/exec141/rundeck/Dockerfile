FROM openjdk:8-jre-alpine  
MAINTAINER Niels van Brecht <docker-rundeck@vanbrecht.family>  
ADD http://dl.bintray.com/rundeck/rundeck-maven/rundeck-launcher-2.10.0.jar
/opt/rundeck/  
WORKDIR /opt/rundeck  
COPY files/ssl.properties /opt/rundeck/  
COPY files/keystore /opt/rundeck/  
EXPOSE 4440 4443  
ENTRYPOINT ["/usr/bin/java","-XX:MaxPermSize=256M", "-Xmx1024M",
"-Drundeck.ssl.config=/opt/rundeck/ssl.properties", "-jar",
"/opt/rundeck/rundeck-launcher-2.10.0.jar"]  

