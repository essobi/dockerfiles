# Version 1.0  
FROM java:openjdk-7-jdk  
  
MAINTAINER kiryuxxu <kiryu@ux-xu.com>  
  
  
ENV GRADLE_VERSION 2.6  
ENV ANDROID_PLATFORM_VERSION 23  
ENV ANDROID_BUILD_TOOOS_REVISION 23.0.2  
ENV ANDROID_SDK_REVISION 24.4.1  
ENV ANDROID_EMULATOR_TARGET_VERSION 22  
# ================================================================  
# apt  
# ================================================================  
RUN dpkg --add-architecture i386  
RUN apt-get update  
RUN apt-get -y install \  
curl \  
unzip \  
libncurses5:i386 \  
libstdc++6:i386 \  
zlib1g:i386  
RUN apt-get clean  
  
# ================================================================  
# gradle  
# ================================================================  
RUN curl -L -O
"http://services.gradle.org/distributions/gradle-$GRADLE_VERSION-all.zip"  
RUN unzip -o "gradle-$GRADLE_VERSION-all.zip"  
RUN mv "gradle-$GRADLE_VERSION" "/usr/local/gradle-$GRADLE_VERSION"  
RUN rm gradle-$GRADLE_VERSION-all.zip  
  
ENV GRADLE_HOME "/usr/local/gradle-$GRADLE_VERSION"  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
  
# ================================================================  
# android sdk  
# ================================================================  
RUN curl -L -O "http://dl.google.com/android/android-
sdk_r$ANDROID_SDK_REVISION-linux.tgz"  
RUN tar -xvzf "android-sdk_r$ANDROID_SDK_REVISION-linux.tgz"  
RUN mv android-sdk-linux /usr/local/android-sdk  
RUN rm android-sdk_r$ANDROID_SDK_REVISION-linux.tgz  
  
ENV ANDROID_HOME /usr/local/android-sdk  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
  
  
# ================================================================  
# android sdk components  
# ================================================================  
ENV ANDROID_SDK_COMPONENTS platform-tools,build-
tools-$ANDROID_BUILD_TOOOS_REVISION,android-$ANDROID_PLATFORM_VERSION,extra-
google-m2repository,extra-android-support,extra-android-m2repository  
RUN echo "y" | android update sdk --no-ui --all --force --filter
$ANDROID_SDK_COMPONENTS  
  
# ================================================================  
# emulator  
# ================================================================  
ENV ANDROID_EMULATOR_ABI armeabi-v7a  
ENV ANDROID_EMULATOR_TARGET_NAME android-emulator  
  
ENV ANDROID_EMULATOR_COMPONENTS android-$ANDROID_EMULATOR_TARGET_VERSION,sys-
img-$ANDROID_EMULATOR_ABI-android-$ANDROID_EMULATOR_TARGET_VERSION  
RUN echo "y" | android update sdk --no-ui --all --force --filter
$ANDROID_EMULATOR_COMPONENTS  
  
# ================================================================  
# scripts  
# ================================================================  
COPY wait-for-emulator /usr/local/bin/  
COPY start-emulator /usr/local/bin/  

