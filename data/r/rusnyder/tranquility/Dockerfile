FROM openjdk:8-jre-alpine  
MAINTAINER Russell Snyder <ru.snyder@gmail.com>  
  
# Java config  
ENV TRANQUILITY_VERSION 0.8.0  
ENV TRANQUILITY_PROPERTIES_ZOOKEEPER_CONNECT zookeeper  
ENV TRANQUILITY_PROPERTIES_HTTP_PORT 8200  
# Install  
RUN apk update \  
&& apk add bash jq \  
&& rm -rf /var/cache/apk/* \  
&& wget -q -O - \  
http://static.druid.io/tranquility/releases/tranquility-
distribution-$TRANQUILITY_VERSION.tgz \  
| tar -xzf - -C /usr/share \  
&& ln -s /usr/share/tranquility-distribution-$TRANQUILITY_VERSION
/usr/share/tranquility  
  
COPY conf /usr/share/tranquility-distribution-$TRANQUILITY_VERSION/conf  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
WORKDIR /usr/share/tranquility  
  
ENTRYPOINT /docker-entrypoint.sh  

