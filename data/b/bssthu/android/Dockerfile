FROM ubuntu:16.04  
MAINTAINER bssthu  
  
# Install java8 and Deps  
RUN apt-get update && \  
apt-get install -y --no-install-recommends software-properties-common && \  
dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y openjdk-8-jdk && \  
apt-get install -y --force-yes --no-install-recommends expect git wget \  
libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 \  
lib32z1 python curl unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Android SDK  
RUN cd /opt && \  
wget --output-document=tools.zip --quiet \  
https://dl.google.com/android/repository/tools_r25.2.5-linux.zip && \  
unzip tools.zip -d android-sdk-linux && \  
rm -f tools.zip && \  
chown -R root.root android-sdk-linux  
  
# Setup environment  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Install sdk elements  
COPY tools /opt/tools  
RUN chmod +x /opt/tools/android-*.sh  
ENV PATH ${PATH}:/opt/tools  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk --all --no-
ui --filter \  
platform-tools,build-tools-25,build-tools-25.0.1,build-tools-25.0.2,build-
tools-25.0.3,\  
android-25,extra-android-support,extra-android-m2repository,\  
extra-google-m2repository,extra-google-google_play_services"]  
  
RUN which adb && \  
which android  
  
# Install Gradle  
WORKDIR /usr/lib  
ENV GRADLE_VERSION 3.3  
RUN cd /usr/lib && \  
wget
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip &&
\  
unzip -q gradle-${GRADLE_VERSION}-all.zip && \  
ln -s "/usr/lib/gradle-${GRADLE_VERSION}" /usr/bin/gradle && \  
rm gradle-${GRADLE_VERSION}-all.zip  
  
ENV GRADLE_HOME /usr/bin/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# GO to workspace  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace  
  

