# wiremock Dockerfile  
#  
# https://github.com/carlosroman/docker-wiremock  
#  
# Pull base image.  
FROM openjdk:8-jre-alpine  
  
ENV WM_PKG_NAME wiremock-standalone  
ENV WM_VERSION 2.7.1  
RUN apk --no-cache --upgrade add ca-certificates \  
&& apk --no-cache --virtual .build-dependencies add wget \  
&& update-ca-certificates --fresh \  
&& mkdir -p /opt/wiremock/ \  
&& wget
https://repo1.maven.org/maven2/com/github/tomakehurst/$WM_PKG_NAME/$WM_VERSION/$WM_PKG_NAME-$WM_VERSION.jar
--progress=bar:force:noscroll -O /opt/wiremock/wiremock.jar \  
&& apk del .build-dependencies  
  
# Define mountable directories.  
VOLUME ["/wiremock/__files", "/wiremock/mappings"]  
  
WORKDIR /wiremock  
  
EXPOSE 8080  
# Define default command.  
ENTRYPOINT ["java", "-jar", "/opt/wiremock/wiremock.jar"]  

