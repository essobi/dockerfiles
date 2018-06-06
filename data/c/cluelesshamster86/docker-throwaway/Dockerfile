  
# ====================================================================== #  
# Android SDK Docker Image  
# ====================================================================== #  
# Base image  
# ---------------------------------------------------------------------- #  
FROM ubuntu:16.04  
# Author  
# ---------------------------------------------------------------------- #  
LABEL maintainer "ivan@aaptiv.com"  
  
# support multiarch: i386 architecture  
# install Java  
# install essential tools  
# install Qt  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y libncurses5:i386 libc6:i386 libstdc++6:i386 lib32gcc1
lib32ncurses5 lib32z1 zlib1g:i386 && \  
apt-get install -y --no-install-recommends openjdk-8-jdk && \  
apt-get install -y git wget zip && \  
apt-get install -y qt5-default  
  
# Download and install Gradle  
ENV GRADLE_VERSION 4.5.1  
RUN cd /opt && \  
wget -q
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip &&
\  
unzip gradle*.zip && \  
ls -d */ | sed 's/\/*$//g' | xargs -I{} mv {} gradle && \  
rm gradle*.zip  
  
# download and install Kotlin compiler  
ENV KOTLIN_VERSION 1.2.10  
RUN cd /opt && \  
wget -q
https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-
compiler-${KOTLIN_VERSION}.zip && \  
unzip *kotlin*.zip && \  
rm *kotlin*.zip  
  
# download and install Android SDK  
ENV ANDROID_SDK_VERSION 3859397  
RUN mkdir -p /opt/android-sdk && cd /opt/android-sdk && \  
wget -q https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_VERSION}.zip && \  
unzip *tools*linux*.zip && \  
rm *tools*linux*.zip  
  
# set the environment variables  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV GRADLE_HOME /opt/gradle  
ENV KOTLIN_HOME /opt/kotlinc  
ENV ANDROID_HOME /opt/android-sdk  
ENV PATH
${PATH}:${GRADLE_HOME}/bin:${KOTLIN_HOME}/bin:${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:${ANDROID_HOME}/tools/bin  
ENV _JAVA_OPTIONS -XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap  
  
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses  
  
CMD ["/bin/bash"]

