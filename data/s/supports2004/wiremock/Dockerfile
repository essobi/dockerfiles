FROM java:8-alpine  
  
RUN apk add --update curl && \  
rm -rf /var/cache/apk/*  
  
ENV WM_PACKAGE wiremock  
ARG WM_VERSION=2.7.1  
RUN mkdir -p /app  
WORKDIR /app  
RUN curl -sSL -o /app/$WM_PACKAGE.jar
https://repo1.maven.org/maven2/com/github/tomakehurst/$WM_PACKAGE-
standalone/$WM_VERSION/$WM_PACKAGE-standalone-$WM_VERSION.jar  
  
EXPOSE 8080  
ENTRYPOINT ["java","-jar","wiremock.jar", "--verbose"]

