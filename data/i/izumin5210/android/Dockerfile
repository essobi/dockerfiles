# Version 1.0  
FROM java:openjdk-7-jdk  
  
MAINTAINER izumin5210 <masayuki@izumin.info>  
  
  
# ================================================================  
# apt  
# ================================================================  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get -y install \  
curl \  
unzip \  
libncurses5:i386 \  
libstdc++6:i386 \  
zlib1g:i386 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# ================================================================  
# gradle  
# ================================================================  
ENV GRADLE_VERSION 2.6  
RUN curl -L -O
"http://services.gradle.org/distributions/gradle-$GRADLE_VERSION-all.zip" \  
&& unzip -o "gradle-$GRADLE_VERSION-all.zip" \  
&& mv "gradle-$GRADLE_VERSION" "/usr/local/gradle-$GRADLE_VERSION" \  
&& rm gradle-$GRADLE_VERSION-all.zip  
  
ENV GRADLE_HOME "/usr/local/gradle-$GRADLE_VERSION"  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
  
# ================================================================  
# android sdk  
# ================================================================  
ENV ANDROID_SDK_REVISION 24.3.4  
RUN curl -L -O "http://dl.google.com/android/android-
sdk_r$ANDROID_SDK_REVISION-linux.tgz" \  
&& tar -xvzf "android-sdk_r$ANDROID_SDK_REVISION-linux.tgz" \  
&& mv android-sdk-linux /usr/local/android-sdk \  
&& rm android-sdk_r$ANDROID_SDK_REVISION-linux.tgz  
  
ENV ANDROID_HOME /usr/local/android-sdk  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
  
  
# ================================================================  
# android sdk components  
# ================================================================  
ENV ANDROID_BUILD_TOOOS_REVISION 23.0.1  
ENV ANDROID_PLATFORM_VERSION 23  
ENV ANDROID_EMULATOR_ABI armeabi-v7a  
ENV ANDROID_EMULATOR_TARGET_NAME android-emulator  
  
RUN echo y | android update sdk --no-ui --all --force --filter \  
platform-tools,build-
tools-$ANDROID_BUILD_TOOOS_REVISION,android-$ANDROID_PLATFORM_VERSION \  
&& echo y | android update sdk --no-ui --all --force --filter \  
extra-google-m2repository,extra-android-support,extra-android-m2repository \  
&& echo y | android update sdk --no-ui --all --force --filter \  
sys-img-$ANDROID_EMULATOR_ABI-android-$ANDROID_PLATFORM_VERSION  
  
# ================================================================  
# scripts  
# ================================================================  
COPY wait-for-emulator /usr/local/bin/  
COPY start-emulator /usr/local/bin/  

