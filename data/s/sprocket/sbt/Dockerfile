FROM openjdk:8-jre-alpine  
  
MAINTAINER Minoru Nakata <minoru@sprocket.bz>  
  
ENV SBT_VERSION=0.13.15  
  
RUN apk add \--no-progress --no-cache --virtual .deps curl tar && \  
apk add \--no-progress --no-cache bash git ncurses openssh && \  
curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/${SBT_VERSION}/sbt-${SBT_VERSION}.tgz" | tar -xz -C /usr/local
\--strip=1 && \  
apk del .deps && \  
sbt sbt-version  

