FROM chrisgarrett/node-dev:8.2.1  
MAINTAINER Chris Garrett (https://github.com/chris-garrett/docker-react-
native-android)  
LABEL description="Container for working with React Native on Android with a
minimal install footprint"  
USER root  
ADD scripts/entry.sh /entry.sh  
  
  
  
##########################################################################################################################  
# OpenJDK verbatim https://github.com/docker-
library/openjdk/blob/b4f29ba829765552239bd18f272fcdaf09eca259/8-jdk/alpine/Dockerfile  
##########################################################################################################################  
#  
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY.  
#  
# A few reasons for installing distribution-provided OpenJDK:  
#  
# 1. Oracle. Licensing prevents us from redistributing the official JDK.  
#  
# 2. Compiling OpenJDK also requires the JDK to be installed, and it gets  
# really hairy.  
#  
# For some sample build times, see Debian's buildd logs:  
# https://buildd.debian.org/status/logs.php?pkg=openjdk-8  
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
ENV JAVA_ALPINE_VERSION 8.131.11-r2  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# If you're reading this and have any feedback on how this image could be  
# improved, please open an issue or a pull request so we can discuss it!  
#  
# https://github.com/docker-library/openjdk/issues  
##########################################################################################################################  
# Android paraphrased https://github.com/yongjhih/docker-alpine-
android/blob/50cc0b4c5ac304be0435fea48caaded8abcf3183/Dockerfile  
##########################################################################################################################  
# https://github.com/yongjhih/docker-android/blob/master/ubuntu-
openjdk-8-android/Dockerfile  
ENV ANDROID_SDK_ZIP http://dl.google.com/android/android-sdk_r24.3.4-linux.tgz  
  
RUN apk add --no-cache curl && \  
mkdir -p /opt && curl -L $ANDROID_SDK_ZIP | tar zxv -C /opt  
# apk add --nocache lib32stdc++6 lib32z1  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
  
# https://github.com/yongjhih/docker-android/blob/master/ubuntu-
openjdk-8-android-extra/Dockerfile  
RUN echo "y" | android update sdk -u -a --filter tools && \  
echo "y" | android update sdk -u -a --filter platform-tools && \  
echo "y" | android update sdk -u -a --filter extra-android-support && \  
echo "y" | android update sdk -u -a --filter extra-android-m2repository && \  
echo "y" | android update sdk -u -a --filter extra-google-google_play_services
&& \  
echo "y" | android update sdk -u -a --filter extra-google-m2repository && \  
echo "y" | android update sdk -u -a --filter extra-google-analytics_sdk_v2  
  
# https://github.com/yongjhih/docker-android/blob/master/ubuntu-
openjdk-8-android-all/Dockerfile  
RUN echo "y" | android update sdk -u -a --filter android-23 && \  
echo "y" | android update sdk -u -a --filter build-tools-23.0.2 && \  
echo "y" | android update sdk -u -a --filter build-tools-23.0.1 && \  
echo "y" | android update sdk -u -a --filter build-tools-23.0.0  
  
  
  
  
  
USER node  

