FROM alpine:3.7  
MAINTAINER bingo <bingo@dankal.cn>  
  
ENV LANG C.UTF-8  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV JAVA_VERSION 8u151  
ENV JAVA_ALPINE_VERSION 8.151.12-r0  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
ENV JAVA_OPTS ""  
ENV TIME_ZONE Asia/Shanghai  
ENV SPRING_PROFILES_ACTIVE dev  
  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home \  
&& apk add --no-cache openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ] \  
&& ln -snf /usr/share/zoneinfo/$TIME_ZONE /etc/localtime \  
&& echo $TIME_ZONE > /etc/timezone  
  
WORKDIR /app  
  
EXPOSE 8080  
CMD java $JAVA_OPTS \  
-jar /app/app.jar \  
\--spring.profiles.active=$SPRING_PROFILES_ACTIVE

