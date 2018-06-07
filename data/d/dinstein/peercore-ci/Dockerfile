FROM ubuntu:xenial  
MAINTAINER Linfeng Liang <lianglinfeng@gmail.com>  
  
RUN apt-get update && apt-get install -y default-jdk && apt-get clean && rm
-rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV HOME /build  
ENV ANDROID_HOME /build-tools/android-sdk  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools:/build-tools/gradle/gradle/bin  
  
WORKDIR /build  

