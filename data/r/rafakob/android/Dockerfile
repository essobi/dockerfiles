FROM ubuntu:16.04  
MAINTAINER Rafał Kobyłko "rafakob@gmail.com"  
# DEPENDENCIES  
RUN dpkg --add-architecture i386 && apt-get update  
RUN apt-get install -yq libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5
lib32z1 python curl nano git --no-install-recommends  
  
# JAVA 8  
RUN echo y | apt-get install openjdk-8-jdk  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# ANDROID SDK  
RUN curl -L "http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz" | tar
--no-same-owner -xz -C /opt  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH $ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH  
  
# ANDROID COMPONENTS  
RUN echo y | android update sdk --no-ui --all --filter \  
addon-google_apis-google-23  
  
RUN echo y | android update sdk --no-ui --all --filter \  
android-23  
  
RUN echo y | android update sdk --no-ui --all --filter \  
tools,build-tools-23.0.3,build-tools-23.0.2,build-tools-23.0.1  
  
RUN echo y | android update sdk --no-ui --all --filter \  
platform-tools,extra-android-m2repository,extra-google-m2repository,extra-
android-support,extra-google-google_play_services  
  
# CLEAN UP  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && apt-get autoremove -y &&
apt-get clean  
  
# SETUP WORKSPACE  
ENV SHELL=/bin/bash TERM=dumb  
RUN mkdir /opt/worksapce  
WORKDIR /opt/workspace  

