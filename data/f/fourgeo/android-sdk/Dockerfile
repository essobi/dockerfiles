FROM ubuntu:16.04  
MAINTAINER Ivan Fastov "c0d3r85@gmail.com"  
RUN apt-get update  
# Install java  
RUN apt-get install -y software-properties-common openjdk-8-jdk-headless  
  
# Install Deps  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
--force-yes expect git wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5
lib32z1 python curl  
  
# Install Android SDK  
RUN cd /opt && wget --output-document=android-sdk.tgz --quiet
http://dl.google.com/android/android-sdk_r24.3.3-linux.tgz  
RUN cd /opt && tar xzf android-sdk.tgz  
#&& chown -R root.root android-sdk-linux  
# Setup environment  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Install sdk elements  
RUN echo y | android update sdk --all --force --no-ui --filter platform-
tools,build-tools-21,build-tools-21.0.1,build-tools-21.0.2,build-
tools-21.1,build-tools-21.1.1,build-tools-21.1.2,build-tools-22,build-
tools-22.0.1,android-21,android-22,addon-google_apis_x86-google-21,extra-
android-support,extra-android-m2repository,extra-google-m2repository,extra-
google-google_play_services  
  
RUN which adb  
RUN which android  
  
RUN rm -f /opt/android-sdk.tgz  
  
# Cleaning  
RUN apt-get clean  
  
# GO to workspace  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace  

