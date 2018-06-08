FROM java:openjdk-8-jre-alpine  
  
ENV FLYWAY_VERSION 4.2.0  
ENV FLYWAY_SQL_DIR /sql  
ENV PATH ${PATH}:/opt/flyway  
  
RUN apk add --no-cache --update openssl make mysql-client  
RUN mkdir /opt \  
&& wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.tar.gz |
tar -xzf- -C /opt \  
&& mv /opt/flyway-${FLYWAY_VERSION} /opt/flyway \  
&& sed -i 's/bash/sh/' /opt/flyway/flyway  
  
ENTRYPOINT ["flyway"]  
WORKDIR /app  

