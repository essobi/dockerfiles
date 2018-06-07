FROM alpine  
MAINTAINER "Riftbit ErgoZ <ergozru@riftbit.com>"  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION=0.34.2  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="blynk" \  
org.label-schema.description="Smallst and Fastest Docker Container with IoT
Blynk Private Server" \  
org.label-schema.url="https://riftbit.com/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/riftbit/docker-blynk" \  
org.label-schema.vendor="Riftbit Studio" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Riftbit ErgoZ"  
  
RUN apk update && apk upgrade && \  
apk add --no-cache --update openjdk8-jre curl unzip && \  
mkdir -p /blynk/data && \  
mkdir /blynk/config && \  
mkdir /logs && \  
touch /logs/server.log && \  
touch /logs/blynk.log && \  
touch /logs/worker.log && \  
curl -L https://github.com/blynkkk/blynk-
server/releases/download/v${VERSION}/server-${VERSION}-java8.jar >
/blynk/server.jar && \  
curl -L https://github.com/blynkkk/blynk-server/archive/v${VERSION}.zip >
/tmp/server.zip && \  
unzip /tmp/server.zip && \  
mv /blynk-server-${VERSION}/server/core/src/main/resources/server.properties
/blynk/config/server.properties && \  
apk del \--purge curl unzip && \  
rm -rf /blynk-server-${VERSION} && \  
rm -rf /var/cache/apk/*  
  
VOLUME ["/blynk/config", "/blynk/data"]  
  
EXPOSE 7443/tcp 8080/tcp 8081/tcp 8082/tcp 8440/tcp 8441/tcp 8442/tcp 8443/tcp
9443/tcp  
  
CMD java -jar /blynk/server.jar -dataFolder /blynk/data -serverConfig
/blynk/config/server.properties > /logs/server.log & \  
tail -f /logs/server.log /logs/blynk.log /logs/worker.log  

