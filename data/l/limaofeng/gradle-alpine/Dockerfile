FROM docker:latest  
MAINTAINER limaofeng <limaofeng@msn.com>  
  
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
  
ENV JAVA_VERSION 8u111  
ENV JAVA_ALPINE_VERSION 8.151.12-r0  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
RUN mkdir /usr/lib/gradle /app  
  
ENV GRADLE_VERSION 2.13  
ENV GRADLE_HOME /usr/lib/gradle/gradle-${GRADLE_VERSION}  
ENV PATH ${PATH}:${GRADLE_HOME}/bin  
  
WORKDIR /usr/lib/gradle  
# 安装 gradle  
RUN set -x \  
&& apk add --no-cache wget \  
&& wget
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip gradle-${GRADLE_VERSION}-bin.zip \  
&& rm gradle-${GRADLE_VERSION}-bin.zip \  
&& apk del wget  
  
# 安装 mysql-client  
RUN apk update && apk add mysql-client && rm -rf /var/cache/apk/*  
  
# 设置 app 目录  
WORKDIR /app  
# 添加 bash  
RUN apk update && apk add bash libstdc++ && rm -rf /var/cache/apk/*  
  
# 设置时区  
RUN apk update && apk add ca-certificates && \  
apk add tzdata && \  
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone  

