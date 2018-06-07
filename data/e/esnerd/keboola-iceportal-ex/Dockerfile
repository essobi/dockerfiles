# instead of maven:3.5.0-jdk-8-alpine, contained old java version  
FROM openjdk:8-jdk-alpine  
RUN apk add --no-cache curl tar bash  
  
ARG MAVEN_VERSION=3.5.0  
ARG USER_HOME_DIR="/root"  
ARG SHA=beb91419245395bd69a4a6edad5ca3ec1a8b64e41457672dc687c173a495f034  
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries  
  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
&& echo "${SHA} /tmp/apache-maven.tar.gz" | sha256sum -c - \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"  
# END maven  
# set switch that enables correct JVM memory allocation in containers  
ENV JAVA_OPTS="-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap"  
ENV MAVEN_OPTS="-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap"  
MAINTAINER David Esner <esnerda@gmail.com>  
ENV APP_VERSION 1.2.0  
RUN apk add --no-cache git  
WORKDIR /home  
RUN git clone https://github.com/davidesner/keboola-iceportal-ex.git ./  
  
RUN mvn compile  
  
ENTRYPOINT mvn -q exec:java -Dexec.args=/data

