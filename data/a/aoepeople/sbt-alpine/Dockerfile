FROM java:openjdk-8-jdk-alpine  
  
MAINTAINER Timo Litzius <timo.litzius@aoe.com>  
  
ENV SBT_VERSION 0.13.15  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash git openssh docker curl tar gzip  
# Install sbt  
RUN curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local && echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built  
  
RUN ln -s /usr/local/sbt-launcher-packaging-$SBT_VERSION/bin/sbt
/usr/local/bin/sbt  
RUN sbt sbt-version  

