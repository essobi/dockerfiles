# https://github.com/ekino/docker-wiremock  
FROM java:8-jre-alpine  
  
RUN \  
apk add --update curl && \  
rm -rf /var/cache/apk/*  
  
ENV WM_PACKAGE wiremock  
ENV WM_VERSION 2.2.1  
RUN mkdir /$WM_PACKAGE  
WORKDIR /$WM_PACKAGE  
RUN curl -sSL -o $WM_PACKAGE.jar
http://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-
standalone/$WM_VERSION/wiremock-standalone-$WM_VERSION.jar  
  
EXPOSE 8080  
# http://wiremock.org/docs/running-standalone/  
CMD ["java", "-jar", "wiremock.jar", "--verbose" ]  

