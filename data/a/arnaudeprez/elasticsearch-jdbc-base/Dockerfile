FROM openjdk:8-jre-alpine  
  
LABEL maintainer="Arnaud Deprez <arnaudeprez@gmail.com>"  
  
ENV DOCKERIZE_VERSION v0.2.0  
#This works with elasticsearch 1.5.2  
ENV ELASTICSEARCH_JDBC_VERSION 1.5.2.0  
# Install dockerize  
RUN apk add --no-cache curl &&\  
curl -sSL
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz -o /tmp/dockerize-linux-
amd64-$DOCKERIZE_VERSION.tar.gz &&\  
tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-
amd64-$DOCKERIZE_VERSION.tar.gz &&\  
rm /tmp/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# Install elasticsearch-jdbc  
RUN curl -sSL
http://xbib.org/repository/org/xbib/elasticsearch/importer/elasticsearch-
jdbc/$ELASTICSEARCH_JDBC_VERSION/elasticsearch-
jdbc-$ELASTICSEARCH_JDBC_VERSION-dist.zip -o /tmp/elasticsearch-
jdbc-$ELASTICSEARCH_JDBC_VERSION-dist.zip &&\  
apk add --no-cache unzip &&\  
unzip -d /opt /tmp/elasticsearch-jdbc-$ELASTICSEARCH_JDBC_VERSION-dist.zip &&\  
apk del unzip &&\  
ln -s /opt/elasticsearch-jdbc-$ELASTICSEARCH_JDBC_VERSION /opt/elasticsearch-
jdbc &&\  
mkdir -p /opt/elasticsearch-jdbc/logs &&\  
touch /opt/elasticsearch-jdbc/logs/jdbc.log  
  
WORKDIR /opt/elasticsearch-jdbc  

