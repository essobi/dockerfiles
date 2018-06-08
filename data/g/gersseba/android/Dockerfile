FROM ubuntu:15.04  
MAINTAINER yewenju <wuyougan@163.com>  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV ANDROID_NDK_HOME /opt/android-ndk-r13b  
ENV GRADLE_USER_HOME /opt/gradle  
  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y curl wget unzip
openjdk-7-jdk openjdk-8-jdk libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5
lib32z1 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN cd /opt && \  
curl -s https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz > android-
sdk.tgz && \  
tar -xvzf android-sdk.tgz && \  
curl -s https://dl.google.com/android/repository/android-
ndk-r13b-linux-x86_64.zip > android-ndk.zip && \  
unzip android-ndk.zip && \  
rm -f android-sdk.tgz android-ndk.zip  
  
RUN mkdir -p ${ANDROID_HOME}/cmake && \  
cd ${ANDROID_HOME}/cmake && \  
curl -s
https://dl.google.com/android/repository/cmake-3.6.3155560-linux-x86_64.zip >
cmake.zip && \  
unzip cmake.zip && \  
rm -f cmake.zip  
  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:${ANDROID_NDK_HOME}  
  
RUN echo y | android update sdk --no-ui --all \--filter \  
build-tools-24.0.0  
  
RUN echo y | android update sdk --no-ui --all \--filter \  
android-24,android-23,android-22,android-21  
  
RUN echo y | android update sdk --no-ui --all \--filter \  
addon-google_apis-google-24,addon-google_apis-google-23,addon-google_apis-
google-22,addon-google_apis-google-21  
  
RUN echo y | android update sdk --no-ui --all \--filter \  
platform-tools,extra-android-m2repository,extra-android-support,extra-google-
google_play_services,extra-google-m2repository  
  
COPY gradle/ /opt/  
  
RUN cd /opt && \  
chmod +x gradlew && \  
bash ./gradle_install.sh 3.3 3.2.1 3.2 3.1 3.0 2.14.1 2.14 2.13 2.12 2.11 && \  
bash ./gradle_plugin.sh 2.2.3 2.2.2 2.2.1 2.2.0 2.1.3 2.1.2 2.1.0 2.0.0 && \  
rm -rf gradle_install.sh gradle_plugin.sh build.gradle gradlew
gradle/wrapper/gradle-wrapper.{jar,properties}  

