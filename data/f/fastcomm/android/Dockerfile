############################################################  
# Dockerfile to build Android APKs  
############################################################  
  
FROM ubuntu:16.04  
MAINTAINER Wimpie Nortje  
  
# Build settings  
ENV GRADLE_VER=4.4 \  
SDK_VER=3859397  
  
# Environment variables  
ENV ANDROID_HOME=/opt/android-sdk-linux \  
PATH=$PATH:/opt/gradle-${GRADLE_VER}/bin \  
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
# Install packages  
## 32 bit libs are for Android tools like aapt which are only available as 32b  
RUN dpkg --add-architecture i386  
RUN apt-get update && apt-get install -y \  
libc6:i386 \  
libncurses5:i386 \  
libstdc++6:i386 \  
lib32z1 \  
libbz2-1.0:i386 \  
git \  
openjdk-8-jdk \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
  
# Fetch Android SDK and Gradle  
## Enable on DockerHub:  
RUN wget --output-document=sdk-tools-linux-${SDK_VER}.zip \  
\--quiet https://dl.google.com/android/repository/sdk-tools-
linux-${SDK_VER}.zip && \  
wget --output-document=gradle-${GRADLE_VER}-bin.zip \  
\--quiet
https://services.gradle.org/distributions/gradle-${GRADLE_VER}-bin.zip  
  
## Enable on local:  
#COPY sdk-tools-linux-${SDK_VER}.zip gradle-${GRADLE_VER}-bin.zip ./  
  
# Install Android SDK to /opt/android-sdk-linux  
RUN mkdir $ANDROID_HOME && \  
unzip sdk-tools-linux-${SDK_VER}.zip -d $ANDROID_HOME && \  
rm sdk-tools-linux-${SDK_VER}.zip && \  
pkgs="platforms;android-14 \  
platforms;android-18 \  
platforms;android-20 \  
platforms;android-23 \  
platforms;android-25 \  
build-tools;27.0.3 \  
platform-tools \  
extras;android;m2repository \  
extras;google;m2repository \  
"; \  
for p in $pkgs; do \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager "$p"; \  
done  
  
# Install Gradle to /opt/gradle-${GRADLE_VER}  
RUN unzip gradle-${GRADLE_VER}-bin.zip && rm gradle-${GRADLE_VER}-bin.zip  
  
WORKDIR /root  

