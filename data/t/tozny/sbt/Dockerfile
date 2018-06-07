# Dockerfile written by Eric Mann <eric@tozny.com>  
#  
# Copyright (c) 2016 Tozny, LLC  
FROM tozny/java  
  
# Set up environment  
ENV SBT_VERSION 0.13.11  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
# Install sbt  
RUN apk add --no-cache curl bash \  
&& curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local \  
&& echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built  
  
MAINTAINER Eric Mann <eric@tozny.com>  
  
# Projects should be copied into this location  
WORKDIR /app

