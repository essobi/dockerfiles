FROM openjdk:8  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -yq libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386
--no-install-recommends && \  
apt-get clean  
  
# Download and untar SDK  
ENV ANDROID_SDK_URL
https://dl.google.com/android/repository/tools_r25.2.3-linux.zip  
RUN curl -L "${ANDROID_SDK_URL}" > android-sdk.zip  
RUN unzip android-sdk.zip -d /usr/local/android-sdk-linux && rm android-
sdk.zip  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV ANDROID_SDK /usr/local/android-sdk-linux  
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:$PATH  
  
# Install Android SDK components  
# License Id: android-sdk-license-ed0d0a5b  
ENV ANDROID_COMPONENTS platform-tools,build-tools-23.0.3,build-
tools-24.0.0,build-tools-24.0.2,android-23,android-24  
# License Id: android-sdk-license-5be876d5  
ENV GOOGLE_COMPONENTS extra-android-m2repository,extra-google-m2repository  
  
RUN echo y | android update sdk --no-ui --all --filter "${ANDROID_COMPONENTS}"
; \  
echo y | android update sdk --no-ui --all --filter "${GOOGLE_COMPONENTS}"  
  
RUN echo y | /usr/local/android-sdk-linux/tools/bin/sdkmanager
"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2"  
RUN echo y | /usr/local/android-sdk-linux/tools/bin/sdkmanager
"extras;m2repository;com;android;support;constraint;constraint-layout-
solver;1.0.2"  
  
# Support Gradle  
ENV TERM dumb  

