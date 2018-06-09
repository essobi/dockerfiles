# Since there is no reason to have curl on the final image, use a multi-stage  
# build to pull down the latest swarm client without needing the dependency.  
FROM alpine:latest  
  
ENV SWARM_CLIENT 3.8  
WORKDIR /  
  
RUN apk add --no-cache curl  
RUN curl -fL -o swarm-client.jar https://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-client/$SWARM_CLIENT/swarm-
client-$SWARM_CLIENT.jar  
RUN apk del curl  
  
# ---  
FROM alpine:edge  
  
LABEL maintainer="evan@swanaudio.com"  
  
RUN apk add --no-cache docker git  
  
# START: https://github.com/docker-
library/openjdk/blob/2598f7123fce9ea870e67f8f9df745b2b49866c0/8-jre/alpine/Dockerfile  
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
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ENV JAVA_VERSION 8u151  
ENV JAVA_ALPINE_VERSION 8.151.12-r0  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8-jre="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
# END: https://github.com/docker-
library/openjdk/blob/2598f7123fce9ea870e67f8f9df745b2b49866c0/8-jre/alpine/Dockerfile  
RUN addgroup -S jenkins && adduser -S -g jenkins -G docker jenkins  
  
WORKDIR /home/jenkins  
  
COPY \--from=0 /swarm-client.jar .  
COPY start-slave.sh /home/jenkins  
  
# Workaround for https://github.com/moby/moby/issues/2259  
RUN mkdir -p /home/jenkins/workspace  
  
# Backport support for docker 17.06 (version used on docker hub)  
RUN chown -R jenkins:jenkins /home/jenkins  
  
VOLUME /home/jenkins/workspace  
  
USER jenkins  
  
# The automatic host discovery feature of jenkins-swarm cannot currently  
# be used with docker-swarm w/ overlay networking, due to:  
# https://github.com/docker/libnetwork/issues/552  
EXPOSE 33848/udp  
  
ENTRYPOINT ["./start-slave.sh"]  

