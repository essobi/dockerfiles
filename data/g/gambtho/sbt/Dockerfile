FROM openjdk:8-jre-alpine  
  
ENV SBT_VERSION 0.13.8  
RUN apk add --no-cache bash curl openrc git && \  
curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local && \  
ln -s /usr/local/sbt/bin/sbt /usr/local/bin/sbt && \  
chmod 0755 /usr/local/bin/sbt  
  
RUN sbt  

