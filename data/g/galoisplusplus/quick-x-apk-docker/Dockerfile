FROM ubuntu:14.04  
  
MAINTAINER galois "yszheda@gmail.com"  
  
########################################  
# Set environments  
ENV ANT_ROOT /usr/bin  
ENV ANDROID_SDK_ROOT /opt/android-sdk-linux  
ENV ANDROID_NDK_ROOT /opt/android-ndk-r10e  
ENV NDK_ROOT /opt/android-ndk-r10e  
ENV GLFW_VERSION "3.0.4"  
ENV GLFW_SOURCE "https://codeload.github.com/glfw/glfw/tar.gz/${GLFW_VERSION}"  
# Set cocos2d-x environment  
# Only need cocos2d-console since the source code of cocos2d-x will be
included in your project.  
ENV COCOS_X_CONSOLE_ROOT /opt/cocos2d-console-3/bin  
ENV PATH
${PATH}:${ANDROID_SDK_ROOT}:${ANDROID_SDK_ROOT}/tools:${ANDROID_NDK_ROOT}:${COCOS_X_CONSOLE_ROOT}  
  
########################################  
# Install required packages  
# NOTE: add "RUN DEBIAN_FRONTEND=noninteractive" to set noninteractive ENV for
the command.  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq \  
# Install add-apt-repository  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install python-software-
properties software-properties-common \  
# Install oracle java  
&& echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections \  
&& echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-
selections \  
&& DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:webupd8team/java \  
&& apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential \  
wget \  
zip \  
unzip \  
php5 \  
python \  
oracle-java6-installer \  
ant \  
libx11-dev \  
libxmu-dev \  
libglu1-mesa-dev \  
libgl2ps-dev \  
libxi-dev \  
g++ \  
libzip-dev \  
libpng12-dev \  
libcurl4-gnutls-dev \  
libfontconfig1-dev \  
libsqlite3-dev \  
libglew*-dev \  
libssl-dev \  
libgnutls-dev \  
xorg-dev \  
libglu1-mesa-dev \  
cmake \  
lib32stdc++6 \  
lib32z1 \  
# Install Android SDK  
&& cd /opt && wget -q https://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz -O android-sdk.tgz \  
&& tar -zxvf android-sdk.tgz \  
&& rm -f android-sdk.tgz \  
&& echo y | android update sdk --no-ui --all --filter platform-tools | grep
'package installed' \  
&& echo y | android update sdk --no-ui --all --filter extra-android-support |
grep 'package installed' \  
&& echo y | android update sdk --no-ui --all --filter android-20 | grep
'package installed' \  
&& echo y | android update sdk --no-ui --all --filter build-tools-20.0.0 |
grep 'package installed' \  
# Install Android NDK  
&& cd /opt && wget -q http://dl.google.com/android/repository/android-
ndk-r10e-linux-x86_64.zip -O android-ndk.zip \  
&& unzip -q android-ndk.zip \  
&& rm -f android-ndk.zip \  
# Install glfw  
&& mkdir /opt/glfw \  
&& cd /opt/glfw \  
&& wget -q https://codeload.github.com/glfw/glfw/tar.gz/${GLFW_VERSION} -O
glfw.tar.gz \  
&& tar xzf glfw.tar.gz \  
&& cd ./glfw-${GLFW_VERSION} \  
&& cmake -G "Unix Makefiles" -DBUILD_SHARED_LIBS=ON \  
&& make \  
&& make install \  
&& ldconfig \  
&& rm -rf /opt/glfw \  
&& cd /opt \  
&& wget https://codeload.github.com/cocos2d/cocos2d-console/tar.gz/v3 -O
cocos2d-console.tar.gz \  
&& tar zxf cocos2d-console.tar.gz \  
&& rm -rf cocos2d-console.tar.gz \  
# Cleaning  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Set project path  
WORKDIR /opt/proj  
  
ENTRYPOINT ["/bin/bash", "cocos", "-m", "debug", "-p", "android", "--compile-
script", "0"]  

