FROM ubuntu:latest  
MAINTAINER Steven Jackson <sj@oscode.net>  
  
RUN apt-get update \  
&& apt-get -y install unzip curl python build-essential  
  
ENV ANDROID_NDK_VERSION r13b  
ENV NDK_HOME ~/ndk  
ENV ANDROID_API 21  
ENV ANDROID_NDK_URL http://dl.google.com/android/repository/android-
ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip  
  
RUN cd tmp \  
&& curl -o ndk.zip ${ANDROID_NDK_URL} \  
&& unzip ndk.zip \  
&& rm ndk.zip \  
&& android-ndk-${ANDROID_NDK_VERSION}/build/tools/make_standalone_toolchain.py
\  
\--arch arm \  
\--api ${ANDROID_API} \  
\--install-dir ${NDK_HOME} \  
&& rm -rf android-ndk-${ANDROID_NDK_VERSION}  
  
ENV PATH ${NDK_HOME}:$PATH  
  
WORKDIR "${NDK_HOME}"  

