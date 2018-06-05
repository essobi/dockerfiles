# Use the latest official OpenJDK 8 image as base.  
FROM openjdk:8-jdk  
  
# Part 1: Gradle  
ENV GRADLE_VERSION 3.3  
ENV GRADLE_HOME /opt/gradle-${GRADLE_VERSION}  
ENV PATH ${PATH}:${GRADLE_HOME}/bin  
  
ENV GRADLE_FILENAME gradle-${GRADLE_VERSION}-bin.zip  
RUN cd /opt \  
&& wget -N -nv https://services.gradle.org/distributions/${GRADLE_FILENAME} \  
&& unzip ${GRADLE_FILENAME} \  
&& rm ${GRADLE_FILENAME}  
  
# Part 2: Android SDK  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
ENV ANDROID_SDK_BASE_URL https://dl.google.com/android/repository/  
ENV ANDROID_SDK_FILENAME tools_r25.2.3-linux.zip  
  
# Android SDK components to install  
#  
# To list available components, try:  
#  
# android list sdk --no-ui --all --extended  
# android list sdk --no-ui --all --extended | grep '^id:'  
# Core tools  
ENV ANDROID_COMPONENTS tools,platform-tools  
# Build tools  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},build-tools-26.0.1  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},build-tools-26.0.0  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},build-tools-25.0.3  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},build-tools-25.0.2  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},build-tools-25.0.1  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},build-tools-25.0.0  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},build-tools-24.0.3  
# Platforms  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},android-26  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},android-25  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},android-24  
# Android Support Repository  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},extra-android-m2repository  
# Google Repository  
ENV ANDROID_COMPONENTS ${ANDROID_COMPONENTS},extra-google-m2repository  
  
# Download the Android SDK and components.  
#  
# Note: The tar extract and "android update sdk" commands MUST all happen in  
# one single RUN step to avoid AUFS filesystem hardlink failures.  
#  
# See: https://code.google.com/p/android/issues/detail?id=183131#c15  
#  
RUN mkdir -p ${ANDROID_HOME} \  
&& cd ${ANDROID_HOME} \  
&& wget -N -nv ${ANDROID_SDK_BASE_URL}${ANDROID_SDK_FILENAME} \  
&& unzip ${ANDROID_SDK_FILENAME} \  
&& rm ${ANDROID_SDK_FILENAME} \  
&& ( echo y | android update sdk --no-ui --all --filter ${ANDROID_COMPONENTS}
)  

