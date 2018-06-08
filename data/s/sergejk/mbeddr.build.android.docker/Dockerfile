FROM mbeddr/mbeddr.build.docker  
MAINTAINER Sergej Koscejev <sergej@koscejev.cz>  
  
# ver 26.1.1  
ENV ANDROID_TOOLS_VERSION_ID 4333796  
ENV ANDROID_HOME /opt/android  
  
ENV ANDROID_NDK_VERSION 16b  
ENV ANDROID_NDK_HOME /opt/android-ndk  
  
# SDK  
RUN curl --silent --show-error --output /tmp/tools.zip
https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_TOOLS_VERSION_ID}.zip && \  
unzip -q /tmp/tools.zip -d ${ANDROID_HOME} && rm /tmp/tools.zip  
  
# Android Licenses  
COPY licenses ${ANDROID_HOME}/licenses  
  
# NDK  
RUN curl --silent --show-error --output /tmp/ndk.zip
https://dl.google.com/android/repository/android-
ndk-r${ANDROID_NDK_VERSION}-linux-x86_64.zip && \  
unzip -q /tmp/ndk.zip -d /tmp && mv /tmp/android-ndk-r${ANDROID_NDK_VERSION}
${ANDROID_NDK_HOME} && rm /tmp/ndk.zip  
  
# Use Java 8 instead of the default Java 7  
RUN update-alternatives --set java /usr/lib/jvm/java-8-openjdk-
amd64/jre/bin/java  
  
# Doxygen & Graphviz  
RUN apt-get update && apt-get install -y doxygen graphviz  
  

