FROM nao20010128nao/android-build:latest  
MAINTAINER nao20010128nao  
  
ENV ANDROID_NDK_HOME /opt/android-ndk  
ENV PATH ${PATH}:${ANDROID_NDK_HOME}  
ENV PATH ${PATH}:${ANDROID_HOME}/cmake/bin  
  
RUN apt-get update -qq && \  
  
mkdir /opt/android-ndk-tmp && \  
cd /opt/android-ndk-tmp && wget -q
https://dl.google.com/android/repository/android-ndk-r13b-linux-x86_64.zip &&
\  
cd /opt/android-ndk-tmp && unzip -q android-ndk-r13b-linux-x86_64.zip && \  
cd /opt/android-ndk-tmp && mv ./android-ndk-r13b ${ANDROID_NDK_HOME} && \  
rm -rf /opt/android-ndk-tmp && \  
  
mkdir /opt/android-cmake-tmp && \  
cd /opt/android-cmake-tmp && wget -q
https://dl.google.com/android/repository/cmake-3.6.3155560-linux-x86_64.zip -O
android-cmake.zip && \  
cd /opt/android-cmake-tmp && unzip -q android-cmake.zip -d android-cmake && \  
cd /opt/android-cmake-tmp && mv ./android-cmake ${ANDROID_HOME}/cmake && \  
rm -rf /opt/android-cmake-tmp && \  
  
apt-get clean  

