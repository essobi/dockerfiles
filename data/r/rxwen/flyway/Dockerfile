FROM anapsix/alpine-java  
MAINTAINER Raymond Wen  
  
ENV VERSION 5.0.4  
RUN apk update && apk add ca-certificates openssl wget curl && update-ca-
certificates  
RUN curl https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/${VERSION}/flyway-commandline-${VERSION}.tar.gz | tar xvz  
RUN mv flyway-${VERSION} flyway  
ENV PATH=${PATH}:/flyway  
  
CMD ["flyway", "--help"]  

