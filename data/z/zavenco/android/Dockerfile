FROM ubuntu:16.04  
  
LABEL vendor="Zaven Sp. z o.o."  
LABEL version="1.0.0"  
LABEL description="Build and testing environment for Android apps"  
# Install system dependencies  
RUN apt-get update && \  
dpkg --add-architecture i386 && \  
apt-get install -y --force-yes --no-install-recommends software-properties-
common nasm openssh-client unzip expect git wget libc6-i386 lib32stdc++6
lib32gcc1 lib32ncurses5 lib32z1 python curl libqt5widgets5 && \  
apt-get clean && \  
rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
# Setup openssh  
eval $(ssh-agent -s) && \  
mkdir -p ~/.ssh && \  
# Install OpenJDK  
add-apt-repository -y ppa:openjdk-r/ppa && \  
apt-get update && \  
apt-get install -y --no-install-recommends openjdk-8-jdk && \  
# Script from official openjdk image to get cross-architecture-safe JAVA_HOME  
{ \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home && \  
chmod +x /usr/local/bin/docker-java-home && \  
ln -svT "/usr/lib/jvm/java-7-openjdk-$(dpkg --print-architecture)" /docker-
java-home  
  
# Copy install tools  
COPY tools /opt/tools  
  
# Export variables  
ENV PATH ${PATH}:/opt/tools  
ENV ANDROID_HOME /opt/tools  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools/:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/emulator  
  
# Download Android SDK  
RUN wget --output-document=android-sdk.tgz --quiet
https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \  
unzip android-sdk.tgz && mv ./tools /opt/tools && \  
# Install and update tools  
mkdir /root/.android && echo 'count=0' > /root/.android/repositories.cfg && \  
echo yes | sdkmanager "tools" && \  
echo yes | sdkmanager "platform-tools" && \  
echo yes | sdkmanager "build-tools;27.0.3" && \  
echo yes | sdkmanager "build-tools;27.0.1" && \  
echo yes | sdkmanager "build-tools;27.0.0" && \  
echo yes | sdkmanager "build-tools;26.0.2" && \  
echo yes | sdkmanager "build-tools;26.0.1" && \  
echo yes | sdkmanager "build-tools;26.0.0" && \  
echo yes | sdkmanager "build-tools;25.0.3" && \  
echo yes | sdkmanager "build-tools;25.0.1" && \  
echo yes | sdkmanager "build-tools;25.0.0" && \  
echo yes | sdkmanager "build-tools;24.0.3" && \  
echo yes | sdkmanager "build-tools;23.0.3" && \  
echo yes | sdkmanager "build-tools;22.0.1" && \  
echo yes | sdkmanager "platforms;android-27" && \  
echo yes | sdkmanager "platforms;android-26" && \  
echo yes | sdkmanager "platforms;android-25" && \  
echo yes | sdkmanager "platforms;android-24" && \  
echo yes | sdkmanager "platforms;android-23" && \  
echo yes | sdkmanager "platforms;android-22" && \  
echo yes | sdkmanager "platforms;android-21" && \  
echo yes | sdkmanager "extras;android;m2repository" && \  
echo yes | sdkmanager "extras;google;google_play_services" && \  
echo yes | sdkmanager "extras;google;m2repository" && \  
echo yes | sdkmanager
"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2"
&& \  
echo yes | sdkmanager
"extras;m2repository;com;android;support;constraint;constraint-layout-
solver;1.0.2" && \  
echo yes | sdkmanager "system-images;android-24;google_apis;x86_64" && \  
# Fix QT by copying libs to local directory  
cp -a $ANDROID_HOME/emulator/lib64/qt/lib/. /usr/lib/x86_64-linux-gnu && \  
# Create AVD  
echo no | avdmanager create avd -n test -k "system-
images;android-24;google_apis;x86_64" -f --abi "x86_64" \--tag "google_apis"
&& \  
# Set workspace  
mkdir -p /opt/workspace  
  
WORKDIR /opt/workspace  

