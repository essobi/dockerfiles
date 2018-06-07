# based on https://github.com/gfx/docker-android-
project/blob/master/Dockerfile  
FROM ubuntu:16.04  
MAINTAINER doubletrouble <zhangqingcai0815@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN dpkg --add-architecture i386 && \  
apt-get -qq update && \  
apt-get -qqy install libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386
curl bzip2 xz-utils wget tar unzip git --no-install-recommends && \  
apt-get clean  
  
# Download and Install Open-JDK-8  
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
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
ENV JAVA_VERSION 8u91  
ENV JAVA_DEBIAN_VERSION 8u91-b14-0ubuntu4~16.04.1  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20160321  
RUN set -x \  
&& apt-get -qq update \  
&& apt-get -qqy install -y \  
openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \  
&& rm -rf /var/lib/apt/lists/* \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
# Download and untar SDK  
ENV ANDROID_SDK_URL http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz  
RUN curl -L "${ANDROID_SDK_URL}" | tar --no-same-owner -xz -C /usr/local  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV ANDROID_SDK /usr/local/android-sdk-linux  
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:$PATH  
  
# Install Android SDK components  
# License Id: android-sdk-license-ed0d0a5b  
ENV ANDROID_COMPONENTS platform-tools,build-tools-23.0.3,build-
tools-24.0.0,android-23,android-24  
# License Id: android-sdk-license-5be876d5  
ENV GOOGLE_COMPONENTS extra-android-m2repository,extra-google-m2repository  
  
RUN echo y | android update sdk --no-ui --all --filter "${ANDROID_COMPONENTS}"
; \  
echo y | android update sdk --no-ui --all --filter "${GOOGLE_COMPONENTS}"  
  
# Download and unzip Gradle  
ENV GRADLE_VERSION 2.14  
ENV GRADLE_SDK_URL
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip  
RUN curl -L "${GRADLE_SDK_URL}" -o gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip gradle-${GRADLE_VERSION}-bin.zip -d /usr/local \  
&& rm -rf gradle-${GRADLE_VERSION}-bin.zip  
ENV GRADLE_HOME /usr/local/gradle-${GRADLE_VERSION}  
ENV PATH ${GRADLE_HOME}/bin:$PATH  
  
ENV TERM dumb

