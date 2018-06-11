FROM openjdk:8-jre-alpine  
  
MAINTAINER Fabio Uechi  
  
ENV WM_PACKAGE wiremock  
ENV WM_VERSION 2.4.1  
RUN mkdir -p /$WM_PACKAGE/bin && \  
mkdir -p /$WM_PACKAGE/config && \  
wget -O /$WM_PACKAGE/bin/$WM_PACKAGE.jar
http://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-
standalone/$WM_VERSION/wiremock-standalone-$WM_VERSION.jar  
  
VOLUME /$WM_PACKAGE/config  
  
EXPOSE 8080  
WORKDIR /$WM_PACKAGE  
  
ENTRYPOINT ["java","-jar","bin/wiremock.jar","--root-dir", "/wiremock/config"]

