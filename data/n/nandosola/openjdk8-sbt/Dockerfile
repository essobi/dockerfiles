FROM nandosola/pimped-alpine  
MAINTAINER Nando Sola <nando@graphenedb.com>  
  
####################################################################################  
# Usage:  
# docker run -v /path/to/scala/repo:/app -ti graphenedb/openjdk8-sbt  
#  
####################################################################################  
# Inspired by  
# https://github.com/cloudbees/java-build-tools-
dockerfile/blob/master/Dockerfile  
# https://github.com/William-Yeh/docker-sbt/blob/master/Dockerfile  
# https://github.com/docker-
library/openjdk/blob/master/8-jdk/alpine/Dockerfile  
####################################################################################  
  
# Check https://pkgs.alpinelinux.org/package/edge/community/x86/openjdk8-jre
for new versions  
ENV JAVA_VERSION 8u144  
ENV JAVA_ALPINE_VERSION 8.144.01-r0  
  
ENV LANG C.UTF-8  
ENV ARCH amd64  
  
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
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# SBT  
ENV SBT_VERSION 0.13.12  
ENV SBT_JAR https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/$SBT_VERSION/sbt-launch.jar  
  
  
#==============================================  
# Add 'ci' user to run tests  
# This adds compatibility with our CI process  
#==============================================  
RUN addgroup -g 1000 ci && \  
adduser -s /bin/bash -h /home/ci -D -u 1000 -G ci ci  
  
#==========================  
# Get SBT and dependencies  
#==========================  
ADD $SBT_JAR /usr/local/bin/sbt-launch.jar  
COPY bin/sbt.sh /usr/local/bin/sbt  
RUN chmod a+x /usr/local/bin/sbt &&\  
chmod a+r /usr/local/bin/sbt-launch.jar  
  
RUN echo "==> fetch all sbt jars from Maven repo..." && \  
echo "==> [CAUTION] this may take several minutes!!!" && \  
su -c '/usr/local/bin/sbt version' \- ci  
  
#=============  
# Final setup  
#=============  
USER ci  
  
VOLUME [ "/app" ]  
WORKDIR /app  
  
ENTRYPOINT ["/usr/local/bin/sbt"]  

