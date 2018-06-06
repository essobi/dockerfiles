FROM java:8  
MAINTAINER cliffred  
  
# Install Dependencies  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
--force-yes libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1  
  
# Cleaning  
RUN apt-get clean  
  
ENV ANDROID_SDK_VERSION 25.2.5  
ENV ANDROID_SDK_URL
https://dl.google.com/android/repository/tools_r${ANDROID_SDK_VERSION}-linux.zip  
ENV ANDROID_API_LEVELS android-25  
ENV ANDROID_BUILD_TOOLS_VERSION 25.0.2  
# Install Android SDK  
RUN cd /opt && wget --quiet --output-document=sdk.zip ${ANDROID_SDK_URL}  
RUN cd /opt && unzip -q sdk.zip -d android && rm -f sdk.zip  
  
# Setup environment  
ENV ANDROID_HOME /opt/android  
ENV PATH ${PATH}:${ANDROID_HOME}/tools  
  
# Install SDK elements  
RUN echo y | android update sdk --all --no-ui --filter tools,platform-
tools,build-tools-${ANDROID_BUILD_TOOLS_VERSION},${ANDROID_API_LEVELS},extra-
android-m2repository  

