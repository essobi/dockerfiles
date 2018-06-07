FROM ubuntu:14.04  
MAINTAINER GreenWang  
  
# Set LC_ALL  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8  
  
WORKDIR /opt  
  
# Add i386 as Android SDK contains 32b binaries  
RUN dpkg --add-architecture i386  
  
# Use tsinghua ubuntu mirror  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted
universe multiverse" > /etc/apt/sources.list && \  
# echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# apt-get update -qq  
RUN apt-get update -qq  
  
# Install common tools  
RUN apt-get install -qqy wget git unzip  
  
# Install ruby  
RUN apt-get install -qqy build-essential curl python-setuptools ruby2.0 \  
&& ln -sf ruby2.0 /usr/bin/ruby \  
&& ln -sf gem2.0 /usr/bin/gem  
  
# Install bundler  
RUN gem install bundler  
  
# Install Android SDK dependencies  
RUN apt-get install -qqy lib32stdc++6 lib32z1 openjdk-7-jdk  
  
# Install Android command line tools, see
http://developer.android.com/sdk/index.html#downloads  
RUN wget -q http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \  
tar xf android-sdk_r24.4.1-linux.tgz && \  
rm -f android-sdk_r24.4.1-linux.tgz  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH $ANDROID_HOME/tools:$PATH  
  
# Install latest platform-tools, build-tools, android platforms, android
support library and google repository.  
RUN ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | \  
android update sdk -u -a -t \  
platform-tools,build-tools-22.0.0,build-tools-22.0.1,build-tools-23.0.0,build-
tools-23.0.1,build-tools-23.0.2,build-
tools-23.0.3,android-18,android-19,android-20,android-21,android-22,android-23,extra-
android-m2repository,extra-android-support,extra-google-m2repository  
ENV PATH $ANDROID_HOME/platform-tools:$PATH  
ENV PATH $ANDROID_HOME/build-tools/23.0.3:$PATH  
  
# Install Android NDK dependencies  
RUN apt-get install -y make  
  
# Install Android NDK, see
http://developer.android.com/ndk/downloads/index.html  
RUN wget -q https://dl.google.com/android/repository/android-
ndk-r12b-linux-x86_64.zip && \  
unzip android-ndk-r12b-linux-x86_64.zip && \  
rm -f android-ndk-r12b-linux-x86_64.zip  
ENV ANDROID_NDK_HOME /opt/android-ndk-r12b  
ENV PATH $ANDROID_NDK_HOME:$PATH  
  
# Test NDK  
RUN which ndk-build  
  
# Install gradle  
RUN wget -q https://services.gradle.org/distributions/gradle-2.10-bin.zip && \  
unzip gradle-2.10-bin.zip && \  
rm -f gradle-2.10-bin.zip  
ENV GRADLE_HOME /opt/gradle-2.10  
ENV PATH $GRADLE_HOME/bin:$PATH  
  
# Set workspace  
RUN mkdir -p /home/ci  
WORKDIR /home/ci  

