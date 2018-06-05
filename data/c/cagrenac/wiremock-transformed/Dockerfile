FROM openjdk:8-jre  
  
MAINTAINER Ilia Korolev <tabemononari@gmail.com>  
  
ENV WM_PACKAGE wiremock  
  
ARG WM_VERSION=2.15.0  
RUN mkdir ~/$WM_PACKAGE  
  
WORKDIR ~/$WM_PACKAGE  
  
RUN curl -sSL -o $WM_PACKAGE.jar
https://repo1.maven.org/maven2/com/github/tomakehurst/$WM_PACKAGE-
standalone/$WM_VERSION/$WM_PACKAGE-standalone-$WM_VERSION.jar  
  
ENV BT_PACKAGE body-transformer  
  
ARG BT_VERSION=1.1.6  
RUN curl -sSL -o $BT_PACKAGE.jar https://github.com/opentable/wiremock-body-
transformer/releases/download/wiremock-body-transformer-$BT_VERSION/wiremock-
body-transformer-$BT_VERSION.jar  
  
EXPOSE 8080  
CMD java -cp "body-transformer.jar:wiremock.jar"
com.github.tomakehurst.wiremock.standalone.WireMockServerRunner --verbose
--extensions com.opentable.extension.BodyTransformer  

