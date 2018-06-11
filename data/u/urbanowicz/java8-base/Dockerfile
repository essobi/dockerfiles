FROM alpine  
  
RUN apk --no-cache add \  
curl \  
openssl \  
openjdk8-jre \  
mysql-client \  
nginx \  
ttf-dejavu \  
&& mkdir /run/nginx  
  
COPY jfx.jar /usr/lib/jvm/java-1.8-openjdk/jre/lib/ext/jfx.jar  
  
ENV DOCKERIZE_VERSION v0.5.0  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-$DOCKERIZE_VERSION.tar.gz \  
&& rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
ENV FLYWAY_VERSION 3.2.1  
ENV MYSQL_CONNECTOR_VERSION 5.1.41  
  
RUN mkdir -p /usr/lib/flyway/jar \  
&& mkdir -p /usr/lib/flyway/drivers \  
&& mkdir -p /usr/lib/flyway/jars \  
&& wget -O /usr/lib/flyway/jar/flyway-cmd.jar
https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/$FLYWAY_VERSION/flyway-commandline-$FLYWAY_VERSION.jar \  
&& wget -O /usr/lib/flyway/jar/flyway-core.jar
https://repo1.maven.org/maven2/org/flywaydb/flyway-
core/$FLYWAY_VERSION/flyway-core-$FLYWAY_VERSION.jar \  
&& wget -O /usr/lib/flyway/drivers/mysql.jar
https://repo1.maven.org/maven2/mysql/mysql-connector-
java/$MYSQL_CONNECTOR_VERSION/mysql-connector-
java-$MYSQL_CONNECTOR_VERSION.jar  

