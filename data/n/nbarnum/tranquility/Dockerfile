FROM openjdk:8-jre-alpine  
MAINTAINER nbarnum <nbarnum@users.noreply.github.com>  
  
ARG TRANQUILITY_HOME=/usr/local/tranquility  
ARG TRANQUILITY_VERSION=0.8.2  
RUN mkdir -p $TRANQUILITY_HOME/extensions \  
$TRANQUILITY_HOME/var/tmp && \  
wget -q -O - "http://static.druid.io/tranquility/releases/tranquility-
distribution-$TRANQUILITY_VERSION.tgz" \  
| tar zxf - --strip-components 1 -C $TRANQUILITY_HOME && \  
apk add --no-cache bash  
  
VOLUME ["$TRANQUILITY_HOME/conf", "$TRANQUILITY_HOME/extensions"]  
  
COPY server.json $TRANQUILITY_HOME/conf/server.json  
  
WORKDIR $TRANQUILITY_HOME  
  
EXPOSE 8200  
ENTRYPOINT ["bin/tranquility"]  

