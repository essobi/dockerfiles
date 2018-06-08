FROM java:openjdk-8-jdk  
  
MAINTAINER limaofeng <limaofeng@msn.com>  
  
RUN mkdir /usr/lib/gradle /workspace  
  
ENV GRADLE_VERSION 2.13  
ENV GRADLE_HOME /usr/lib/gradle/gradle-${GRADLE_VERSION}  
ENV PATH ${PATH}:${GRADLE_HOME}/bin  
ENV ANDROID_HOME /usr/lib/android-sdk-linux  
# 设置时区  
RUN apt-get install tzdata && \  
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone  
  
WORKDIR /usr/lib/gradle  
# 安装 gradle  
RUN set -x && \  
wget
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip &&
\  
unzip gradle-${GRADLE_VERSION}-bin.zip && \  
rm gradle-${GRADLE_VERSION}-bin.zip  
  
# 安装 android 环境  
RUN cd /usr/lib/ && \  
set -x && \  
wget --quiet --output-document=android-sdk.tgz
https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \  
tar --extract --gzip --file=android-sdk.tgz && \  
echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter android-23 && \  
echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter platform-tools && \  
echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter build-tools-23.0.3 && \  
echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter extra-android-m2repository && \  
echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter extra-google-google_play_services && \  
echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter extra-google-m2repository && \  
rm android-sdk.tgz && \  
apt-get update && apt-get install -y libc6-i386 lib32stdc++6 lib32gcc1
lib32ncurses5 lib32z1  
  
# 设置 app 目录  
WORKDIR /workspace  

