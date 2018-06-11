FROM wiggins/alpine:3.7  
MAINTAINER from wiggins  
ENV LANG C.UTF-8  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
ENV JAVA_VERSION 8u151  
ENV JAVA_ALPINE_VERSION 8.151.12-r0  
RUN set -x && \  
apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" && \  
rm -rf /var/cache/apk/* && \  
{ \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home && \  
chmod +x /usr/local/bin/docker-java-home && \  
[ "$JAVA_HOME" = "$(docker-java-home)" ]  

