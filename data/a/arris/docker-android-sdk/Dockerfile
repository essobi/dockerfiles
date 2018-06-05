# Some stuff from
https://0xacab.org/leap/bitmask_android/blob/a7b4f463e4ffc282814ef74daf18c74581fc3a7d/docker/android-
sdk.dockerfile  
FROM arris/dev:latest  
  
ARG APT_PACKAGES='unzip openjdk-8-jdk maven make clang lib32stdc++6 lib32z1'  
ARG DEBIAN_FRONTEND=noninteractive  
ENV ANDROID_HOME /opt/android/sdk  
ENV SDK_TOOLS_VERSION "25.2.5"  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
# ENV ANDROID_NDK_HOME ${ANDROID_HOME}/ndk-bundle  
# ENV PATH ${PATH}:${ANDROID_NDK_HOME}  
  
RUN \  
# Apt Packages  
apt-get update -y \  
&& apt-get install -yq ${APT_PACKAGES} \  
&& apt-get clean \  
# Android SDK  
&& mkdir -p ${ANDROID_HOME} \  
&& cd ${ANDROID_HOME} \  
&& wget -q -O sdk-tools.zip
https://dl.google.com/android/repository/tools_r${SDK_TOOLS_VERSION}-linux.zip
\  
&& unzip -q sdk-tools.zip -d ${ANDROID_HOME} \  
&& rm -f sdk-tools.zip \  
# HACK :(  
&& mkdir -p ~/.android && touch ~/.android/repositories.cfg \  
# Install Platform Tools Package  
&& echo y | sdkmanager "platform-tools" \  
# Install Android Support Repositories  
&& echo y | sdkmanager "extras;android;m2repository" \  
# Install Target SDK Packages (Please keep in descending order)  
&& echo y | sdkmanager "platforms;android-25" \  
&& echo y | sdkmanager "platforms;android-24" \  
&& echo y | sdkmanager "platforms;android-23" \  
# Install Build Tools (Please keep in descending order)  
&& echo y | sdkmanager "build-tools;25.0.2" \  
&& echo y | sdkmanager "build-tools;24.0.3" \  
&& echo y | sdkmanager "build-tools;23.0.3"  
# Install NDK packages from sdk tools  
# && echo y | sdkmanager "ndk-bundle"  
# && echo y | sdkmanager "cmake;3.6.3155560"  
# && echo y | sdkmanager "lldb;2.3"  
# --- Install Android Emulator  
# && echo y | sdkmanager "emulator"  
# System Images for emulators  
# && echo y | sdkmanager "system-images;android-25;google_apis;armeabi-v7a"  
# && echo y | sdkmanager "system-images;android-24;google_apis;armeabi-v7a"  
# && echo y | sdkmanager "system-images;android-23;google_apis;armeabi-v7a"  
# && echo y | sdkmanager "system-images;android-23;google_apis;arm64-v8a"  
  
COPY config/android /root/.android  
  

