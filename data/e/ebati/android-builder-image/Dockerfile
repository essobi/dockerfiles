FROM openjdk:8-jdk  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y \  
expect \  
lib32z1 \  
libc6:i386 \  
libncurses5:i386 \  
libstdc++6:i386 \  
tar \  
unzip \  
wget && \  
rm -rf /var/lib/apt/lists/*  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV ANDROID_SDK_TOOLS_VERSION 3859397  
RUN wget -q -O android-sdk.zip https://dl.google.com/android/repository/sdk-
tools-linux-${ANDROID_SDK_TOOLS_VERSION}.zip && \  
unzip android-sdk.zip -d ${ANDROID_HOME} && rm android-sdk.zip  
  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin  
ENV ANDROID_COMPILE_SDK 27  
ENV ANDROID_BUILD_TOOLS 27.0.2  
RUN yes | sdkmanager platform-tools "build-tools;${ANDROID_BUILD_TOOLS}"
"platforms;android-${ANDROID_COMPILE_SDK}" "extras;android;m2repository"
"extras;google;m2repository"  

