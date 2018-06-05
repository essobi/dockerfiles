FROM alpine:latest  
  
RUN apk add --update libreoffice && \  
apk info --purge  
  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.7-openjdk/jre/bin:/usr/lib/jvm/java-1.7-openjdk/bin  
  
ENV JAVA_VERSION 7u91  
ENV JAVA_ALPINE_VERSION 7.91.2.6.3-r2  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk7="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  

