FROM ubuntu:16.04  
  
ARG ANDROID_TARGET_SDK=27  
ARG ANDROID_BUILD_TOOLS=27.0.1  
ARG ANDROID_SDK_TOOLS=3859397  
  
ENV ANDROID_HOME=${PWD}/android-sdk-linux  
ENV PATH=${PATH}:${ANDROID_HOME}/platform-tools  
ENV PATH=${PATH}:${ANDROID_HOME}/tools  
ENV PATH=${PATH}:${ANDROID_HOME}/tools/bin  
ENV PATH=${PATH}:${ANDROID_NDK}  
RUN apt-get update \  
&& apt-get install wget gnupg openjdk-8-jdk unzip -y \  
&& rm -rf /var/cache/apt/archives \  
&& update-ca-certificates \  
&& wget -q -O android-sdk.zip https://dl.google.com/android/repository/sdk-
tools-linux-${ANDROID_SDK_TOOLS}.zip \  
&& mkdir ${ANDROID_HOME} \  
&& unzip -qo android-sdk.zip -d ${ANDROID_HOME} \  
&& chmod +x ${ANDROID_HOME}/tools/android \  
&& rm android-sdk.zip \  
&& mkdir -p ~/.gradle \  
&& echo "org.gradle.daemon=false" >> ~/.gradle/gradle.properties \  
&& mkdir ~/.android \  
&& touch ~/.android/repositories.cfg \  
&& yes | sdkmanager --licenses > /dev/null \  
&& sdkmanager --update > /dev/null \  
&& sdkmanager "platforms;android-${ANDROID_TARGET_SDK}" "build-
tools;${ANDROID_BUILD_TOOLS}" platform-tools tools > /dev/null  

