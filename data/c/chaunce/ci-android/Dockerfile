FROM ubuntu:14.04  
MAINTAINER Chaunce <chang.chaunce@gmail.com>  
  
# Configuration  
ENV JAVA_VERSION openjdk-7-jdk  
ENV GRADLE_VERSION 2.11  
ENV ANDROID_SDK_VERSION 24.4.1  
ENV ANDROID_API_VERSION 23  
ENV ANDROID_BUILDTOOL_VERSION 23.0.2  
  
# Install basic tool  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y wget && \  
apt-get install -y libncurses5:i386 libstdc++6:i386 zlib1g:i386 && \  
apt-get install -y unzip  
  
# Install openJDK Java  
RUN apt-get install -y $JAVA_VERSION  
  
# 安装 Java 7  
RUN wget -q --no-check-certificate -c \--header "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz && \  
tar -xzf jdk-7u79-linux-x64.tar.gz -C /usr/local && \  
rm jdk-7u79-linux-x64.tar.gz && \  
# 安装 Java 8  
wget -q --no-check-certificate -c \--header "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.tar.gz && \  
tar -xzf jdk-8u66-linux-x64.tar.gz -C /usr/local && \  
rm jdk-8u66-linux-x64.tar.gz  
  
# 配置 Java 环境变量  
ENV JAVA7_HOME /usr/local/jdk1.7.0_79  
ENV JAVA8_HOME /usr/local/jdk1.8.0_66  
ENV JAVA_HOME /usr/local/jdk1.7.0_79  
  
# Gradle Environment  
ENV GRADLE_HOME /gradle-${GRADLE_VERSION}  
RUN cd / && \  
wget -q
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip &&
\  
unzip gradle-${GRADLE_VERSION}-all.zip && \  
rm gradle-${GRADLE_VERSION}-all.zip  
  
# Android Environment  
ENV ANDROID_HOME /android_sdk  
RUN cd / && \  
mkdir $ANDROID_HOME && \  
cd $ANDROID_HOME && \  
wget -q http://dl.google.com/android/android-
sdk_r${ANDROID_SDK_VERSION}-linux.tgz && \  
tar -zxf android-sdk_r${ANDROID_SDK_VERSION}-linux.tgz && \  
rm android-sdk_r${ANDROID_SDK_VERSION}-linux.tgz && \  
mv android-sdk-linux/* . && \  
rm -rf android-sdk-linux && \  
  
RUN echo y | tools/android update sdk --no-ui --all \--filter platform-tools
&& \  
echo y | tools/android update sdk --no-ui --all \--filter build-
tools-${ANDROID_BUILDTOOL_VERSION} && \  
echo y | tools/android update sdk --no-ui --all \--filter
android-${ANDROID_API_VERSION} && \  
echo y | tools/android update sdk --no-ui --all \--filter android-22 && \  
echo y | tools/android update sdk --no-ui --all \--filter android-21 && \  
echo y | tools/android update sdk --no-ui --all \--filter android-20 && \  
echo y | tools/android update sdk --no-ui --all \--filter android-19 && \  
echo y | tools/android update sdk --no-ui --all \--filter android-18 && \  
echo y | tools/android update sdk --no-ui --all \--filter android-17 && \  
echo y | tools/android update sdk --no-ui --all \--filter android-16 && \  
echo y | tools/android update sdk --no-ui --all \--filter android-15 && \  
echo y | tools/android update sdk --no-ui --all \--filter extra-
android-m2repository && \  
echo y | tools/android update sdk --no-ui --all \--filter extra-
google-m2repository && \  
echo y | tools/android update sdk --no-ui --all \--filter extra-android-
support  
  
# Environment  
ENV
PATH=$PATH:$JAVA_HOME/bin:$GRADLE_HOME/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:${ANDROID_HOME}/build-tools/${ANDROID_BUILDTOOL_VERSION}  
  
WORKDIR /  
  
  
# RUN dpkg --add-architecture i386 && \  
# apt-get update && \  
# apt-get install -y wget && \  
# apt-get install -y libncurses5:i386 libstdc++6:i386 zlib1g:i386 && \  
# apt-get clean  
  
# # 安装 Java 7  
# RUN wget -q --no-check-certificate -c \--header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz && \  
# tar -xzf jdk-7u79-linux-x64.tar.gz -C /usr/local && \  
# rm jdk-7u79-linux-x64.tar.gz && \  
# # 安装 Java 8  
# wget -q --no-check-certificate -c \--header "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.tar.gz && \  
# tar -xzf jdk-8u66-linux-x64.tar.gz -C /usr/local && \  
# rm jdk-8u66-linux-x64.tar.gz  
  
# # 配置 Java 环境变量  
# ENV JAVA7_HOME /usr/local/jdk1.7.0_79  
# ENV JAVA8_HOME /usr/local/jdk1.8.0_66  
# ENV JAVA_HOME /usr/local/jdk1.7.0_79  
# ENV PATH $PATH:$JAVA_HOME/bin  
  
# 安装 Android SDK  
# RUN wget -q http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \  
# tar -xzf android-sdk_r24.4.1-linux.tgz -C /usr/local && \  
# rm android-sdk_r24.4.1-linux.tgz  
  
# # 配置 Android SDK 环境变量  
# ENV ANDROID_HOME /usr/local/android-sdk-linux  
# ENV PATH $PATH:$ANDROID_HOME/tools  
# ENV PATH $PATH:$ANDROID_HOME/platform-tools  
# ENV PATH $PATH:$ANDROID_HOME/build-tools/23.0.2  
  
# RUN echo yes | android update sdk --no-ui --all \--filter platform-tools &&
\  
# echo yes | android update sdk --no-ui --all \--filter build-tools-23.0.2 &&
\  
# echo yes | android update sdk --no-ui --all \--filter android-23 && \  
# echo yes | android update sdk --no-ui --all \--filter android-22 && \  
# echo yes | android update sdk --no-ui --all \--filter android-21 && \  
# echo yes | android update sdk --no-ui --all \--filter android-20 && \  
# echo yes | android update sdk --no-ui --all \--filter android-19 && \  
# echo yes | android update sdk --no-ui --all \--filter android-18 && \  
# echo yes | android update sdk --no-ui --all \--filter android-17 && \  
# echo yes | android update sdk --no-ui --all \--filter android-16 && \  
# echo yes | android update sdk --no-ui --all \--filter android-15 && \  
# echo yes | android update sdk --no-ui --all \--filter extra-
android-m2repository && \  
# echo yes | android update sdk --no-ui --all \--filter extra-
google-m2repository && \  
# echo yes | android update sdk --no-ui --all \--filter extra-android-support  
  
# # 安装 Android NDK  
# RUN wget -q http://dl.google.com/android/ndk/android-
ndk-r10e-linux-x86_64.bin && \  
# chmod a+x android-ndk-r10e-linux-x86_64.bin && \  
# ./android-ndk-r10e-linux-x86_64.bin -o/usr/local && \  
# rm android-ndk-r10e-linux-x86_64.bin  
  
# # 配置 Android NDK 环境变量  
# ENV NDK_HOME /usr/local/android-ndk-r10e  
# ENV PATH $PATH:$NDK_HOME  

