FROM node:8-alpine  
  
ENV LANG C.UTF-8  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ENV JAVA_VERSION 8u131  
ENV JAVA_ALPINE_VERSION 8.131.11-r2  
  
ENV SDK_TOOLS "3859397"  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV GLIBC_VERSION "2.27-r0"  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Install:  
# OpenJDK  
# from https://github.com/docker-
library/openjdk/blob/2598f7123fce9ea870e67f8f9df745b2b49866c0/8-jdk/alpine/Dockerfile  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home \  
&& set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ] \  
&& apk add --no-cache --virtual=.build-dependencies wget unzip ca-certificates
bash && \  
wget https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub -O /etc/apk/keys/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk -O
/tmp/glibc.apk && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk -O
/tmp/glibc-bin.apk && \  
apk add --no-cache /tmp/glibc.apk /tmp/glibc-bin.apk && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/* && \  
wget http://dl.google.com/android/repository/sdk-tools-linux-${SDK_TOOLS}.zip
-O /tmp/tools.zip && \  
mkdir -p ${ANDROID_HOME} && \  
unzip /tmp/tools.zip -d ${ANDROID_HOME} && \  
rm -v /tmp/tools.zip && \  
mkdir -p /root/.android/ && touch /root/.android/repositories.cfg && \  
yes | ${ANDROID_HOME}/tools/bin/sdkmanager "--licenses" && \  
${ANDROID_HOME}/tools/bin/sdkmanager "--update" && \  
${ANDROID_HOME}/tools/bin/sdkmanager \  
"tools" \  
"platform-tools" \  
"build-tools;25.0.2" \  
"build-tools;26.0.1" \  
"build-tools;23.0.1" \  
"platforms;android-23" \  
"platforms;android-25" \  
"platforms;android-26"  
  
WORKDIR /root  

