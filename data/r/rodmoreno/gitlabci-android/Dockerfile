# Android development environment for drone based on Ubuntu 14.04 LTS.  
# version 0.9.0  
# Start with Ubuntu 14.04 LTS.  
FROM ubuntu:14.04  
MAINTAINER Rodrigo Moreno <rodrigo@chilangolabs.com>  
  
# ANDROID DIRECTORY  
ENV ANDROID_HOME /usr/local/android-sdk  
  
# Never ask for confirmations  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-
set-selections  
  
# Common dependencies  
RUN apt-get update -qq  
RUN apt-get install -y bzip2 git openssh-client python-software-properties
software-properties-common unzip  
  
# Dependencies to execute Android builds  
RUN add-apt-repository ppa:webupd8team/java  
RUN dpkg --add-architecture i386  
RUN apt-get update -qq  
RUN apt-get install -y oracle-java8-installer libc6:i386 libstdc++6:i386
libgcc1:i386 libncurses5:i386 libz1:i386  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Install Android SDK  
RUN wget -q https://dl.google.com/android/repository/tools_r25.2.5-linux.zip
-O android-sdk-tools.zip  
RUN unzip -q android-sdk-tools.zip -d ${ANDROID_HOME}  
RUN rm -f android-sdk-tools.zip  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
# Accept "android-sdk-license" before installing components  
RUN mkdir -p ${ANDROID_HOME}/licenses  
RUN echo 8933bad161af4178b1185d1a37fbf41ea5269c55 >
${ANDROID_HOME}/licenses/android-sdk-license  
  
# Other tools and resources of Android SDK  
RUN sdkmanager "tools"  
RUN sdkmanager "platform-tools"  
  
# SDKs  
RUN sdkmanager "platforms;android-25"  
RUN sdkmanager "platforms;android-24"  
RUN sdkmanager "platforms;android-23"  
  
# Build tools  
RUN sdkmanager "build-tools;25.0.2"  
RUN sdkmanager "build-tools;24.0.3"  
RUN sdkmanager "build-tools;23.0.3"  
  
# Extras  
RUN sdkmanager "extras;android;m2repository"  
RUN sdkmanager "extras;google;m2repository"  
RUN sdkmanager "extras;google;google_play_services"  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout;1.0.2"  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout-solver;1.0.2"  
  
# Google apis  
RUN sdkmanager "add-ons;addon-google_apis-google-24"  
RUN sdkmanager "add-ons;addon-google_apis-google-23"  
  
# Install Gradle  
RUN wget -q https://services.gradle.org/distributions/gradle-3.4.1-bin.zip -O
gradle.zip  
RUN unzip -q gradle.zip  
RUN mv gradle-3.4.1 /usr/local/gradle  
RUN rm gradle.zip  
ENV GRADLE_HOME /usr/local/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Cleaning  
RUN apt-get clean  

