FROM java:8-jre-alpine  
  
MAINTAINER garrett_bates@intuit.com  
  
ENV WM_PACKAGE wiremock  
ENV WM_VERSION 2.1.4-rc3  
  
RUN mkdir /$WM_PACKAGE  
WORKDIR /$WM_PACKAGE  
  
RUN apk update  
RUN apk add ca-certificates  
RUN update-ca-certificates  
  
RUN apk add wget  
  
RUN wget -O $WM_PACKAGE.jar
https://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-
standalone/$WM_VERSION/$WM_PACKAGE-standalone-$WM_VERSION.jar  
  
EXPOSE 8080  
ENTRYPOINT ["java","-jar","wiremock.jar"]  

