FROM alpine:latest  
MAINTAINER Jose Antonio Sanchez <jose.sanchezm@atos.net>  
  
# Install java  
RUN apk --no-cache --update add openjdk8-jre-base  
  
# Prepare configuration  
WORKDIR /etc  
RUN mkdir indigo-reposync  
WORKDIR /etc/indigo-reposync  
COPY ansible/files/docker-java.properties docker-java.properties  
COPY ansible/templates/reposync.properties.j2 reposync.properties  
COPY ansible/files/reposync-log.properties reposync-log.properties  
RUN touch repolist  
  
# Install syncrepo  
COPY docker/reposync-1.0-SNAPSHOT-jar-with-dependencies.jar
/usr/share/reposync/lib/reposync.jar  
COPY docker/reposync.sh /bin/indigo-reposync  
ENTRYPOINT ["indigo-reposync", "start"]  
  

