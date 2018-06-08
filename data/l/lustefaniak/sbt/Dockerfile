# SBT image based on JRE 8  
FROM java:8-jre-alpine  
MAINTAINER Lukas Stefaniak <lustefaniak@gmail.com>  
  
ENV SBT_VERSION 1.1.5  
ENV SCALA_VERSION 2.12.6  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
ENV JAVA_OPTS -Xmx2g  
  
# Install curl  
RUN apk add --update curl bash bc git openssh && rm -rf /var/cache/apk/*  
  
# Install sbt  
RUN curl -sL
"https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz"
| gunzip | tar -x -C /tmp/ && rm -r /usr/local && mv /tmp/sbt /usr/local &&
mkdir $HOME/.sbt && mv /usr/local/lib/local-preloaded $HOME/.sbt/preloaded  
  
RUN mkdir -p src/main/scala && echo "object A" > src/main/scala/A.scala && sbt
'set scalaVersion:="'${SCALA_VERSION}'"' compile && rm -r -f src target
project  
  
WORKDIR /app  

