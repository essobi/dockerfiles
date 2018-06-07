# Builds the Eureka Server using Spring Boot with Docker  
FROM frolvlad/alpine-oraclejdk8:slim  
  
MAINTAINER Gary A. Stafford <garystafford@rochester.rr.com>  
ENV REFRESHED_AT 2016-08-13  
# install jar from GitHub  
ENV GITHUB_REPO=https://github.com/garystafford/microservice-docker-demo-
eureka-server/raw/build-artifacts  
ENV APP_FILE=eureka-server-0.1.0.jar  
  
RUN set -ex \  
&& apk --no-cache add --virtual .build-dependencies curl \  
&& curl -fsSL ${GITHUB_REPO}/${APP_FILE} -o /app.jar \  
&& sh -c 'touch /app.jar'  
  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]  

