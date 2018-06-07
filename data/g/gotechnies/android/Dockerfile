From alpine:3.5  
MAINTAINER Arvind Rawat <arvindr226@gmail.com>  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
RUN apk add --update --no-cache bash libstdc++ libc6-compat libgc++ libgcc
ncurses5-widec-libs ncurses-libs ncurses5-libs zlib wget zip unzip && rm -f
/var/cache/apk/*  
  
##Java JDK 8 ##  
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
  
ENV JAVA_VERSION 8u121  
ENV JAVA_ALPINE_VERSION 8.121.13-r0  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
## End JAVA JDK 8##  
RUN mkdir /opt  
RUN cd /opt \  
&& wget -q https://dl.google.com/android/repository/tools_r25.2.5-linux.zip -O
android-sdk-tools.zip \  
&& unzip -q android-sdk-tools.zip -d ${ANDROID_HOME} \  
&& rm -f android-sdk-tools.zip  
  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
RUN mkdir -p ${ANDROID_HOME}/licenses  
RUN echo 8933bad161af4178b1185d1a37fbf41ea5269c55 >
${ANDROID_HOME}/licenses/android-sdk-license  
  
# Platform tools  
RUN sdkmanager "platform-tools"  
  
# SDKs  
# Please keep these in descending order!  
RUN sdkmanager "platforms;android-25"  
RUN sdkmanager "platforms;android-24"  
RUN sdkmanager "platforms;android-23"  
RUN sdkmanager "platforms;android-22"  
RUN sdkmanager "platforms;android-21"  
RUN sdkmanager "platforms;android-20"  
RUN sdkmanager "platforms;android-19"  
RUN sdkmanager "platforms;android-17"  
RUN sdkmanager "platforms;android-15"  
RUN sdkmanager "platforms;android-10"  
  
# build tools  
# Please keep these in descending order!  
RUN sdkmanager "build-tools;25.0.2"  
RUN sdkmanager "build-tools;24.0.3"  
RUN sdkmanager "build-tools;23.0.3"  
RUN sdkmanager "build-tools;22.0.1"  
RUN sdkmanager "build-tools;21.1.2"  
RUN sdkmanager "build-tools;20.0.0"  
RUN sdkmanager "build-tools;19.1.0"  
RUN sdkmanager "build-tools;17.0.0"  
  
# Android System Images, for emulators  
# Please keep these in descending order!  
RUN sdkmanager "system-images;android-25;google_apis;armeabi-v7a"  
RUN sdkmanager "system-images;android-24;default;armeabi-v7a"  
RUN sdkmanager "system-images;android-22;default;armeabi-v7a"  
RUN sdkmanager "system-images;android-21;default;armeabi-v7a"  
RUN sdkmanager "system-images;android-19;default;armeabi-v7a"  
RUN sdkmanager "system-images;android-17;default;armeabi-v7a"  
RUN sdkmanager "system-images;android-15;default;armeabi-v7a"  
  
# Extras  
RUN sdkmanager "extras;android;m2repository"  
RUN sdkmanager "extras;google;m2repository"  
RUN sdkmanager "extras;google;google_play_services"  
  
# Constraint Layout  
# Please keep these in descending order!  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout;1.0.2"  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout;1.0.1"  
  
# google apis  
# Please keep these in descending order!  
RUN sdkmanager "add-ons;addon-google_apis-google-23"  
RUN sdkmanager "add-ons;addon-google_apis-google-22"  
RUN sdkmanager "add-ons;addon-google_apis-google-21"  
  

