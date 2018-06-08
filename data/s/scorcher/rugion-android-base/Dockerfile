FROM scorcher/rugion-java7:latest  
  
MAINTAINER Nikolay Didenko "nd@info74.ru"  
# Install Deps  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
--force-yes expect git wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5
lib32z1 python curl  
  
# Cleaning  
RUN apt-get clean  
  
# Install Android SDK  
RUN cd /opt && wget --output-document=android-sdk.tgz --quiet
http://dl.google.com/android/android-sdk_r24.4-linux.tgz && tar xzf android-
sdk.tgz && rm -f android-sdk.tgz && chown -R root.root android-sdk-linux  
  
# Setup environment  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Install sdk elements  
COPY tools /opt/tools  
ENV PATH ${PATH}:/opt/tools  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk --all --no-
ui --filter platform-tools,tools,build-tools-21.1.2,build-tools-22,build-
tools-22.0.1,build-tools-23.0.1,android-21,android-22,android-23,addon-
google_apis_x86-google-21,extra-android-support,extra-
android-m2repository,extra-google-m2repository,extra-google-
google_play_services,sys-img-armeabi-v7a-android-21"]  
  
# GO to workspace  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace  

