FROM alpine:3.6  
MAINTAINER Shorn Tolley "bitbucket-shorn@sneakemail.com"  
#############  
# The java stuff below taken from the dockerhub 8u131-jdk-alpine Docker  
# file source code  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ENV JAVA_VERSION 8u131  
ENV JAVA_ALPINE_VERSION 8.131.11-r1  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
#############  
# The awscli stuff below taken from:  
# https://github.com/anigeo/docker-awscli/blob/master/Dockerfile  
# The openrc/docker stuff is from https://wiki.alpinelinux.org/wiki/Docker  
# installs git, aws-cli and docker  
# - openrc is so we can run "rc-udpate", other stuff is aws-cli pre-reqs  
# - bash is installed because the gradle wrapper needs it  
RUN \  
mkdir -p /aws && \  
apk -Uuv add groff less python py-pip openrc docker bash git && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
RUN rc-update add docker boot  
  
# RUN service docker start  

