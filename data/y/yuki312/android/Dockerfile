# Version 1.0.0  
FROM yuki312/android_base  
  
MAINTAINER yuki312 <yuki312.m@gmail.com>  
  
# Never ask for confirmations  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install android sdk  
ENV ANDROID_SDK_VER 24.4.1  
RUN cd / && wget -q http://dl.google.com/android/android-
sdk_r${ANDROID_SDK_VER}-linux.tgz  
RUN tar -xf android-sdk_r${ANDROID_SDK_VER}-linux.tgz \  
&& mv android-sdk-linux /usr/local/android-sdk-linux-r${ANDROID_SDK_VER} \  
&& rm -rf /android-sdk_r${ANDROID_SDK_VER}-linux.tgz  
ENV ANDROID_HOME /usr/local/android-sdk-linux-r${ANDROID_SDK_VER}  
ENV PATH $PATH:${ANDROID_HOME}/tools  
  
# Install android components  
ENV ANDROID_COMPONENTS platform-tools,build-tools-23.0.2,android-23  
ENV GOOGLE_COMPONENTS extra-android-m2repository,extra-google-m2repository  
RUN echo y | android update sdk --no-ui --all --filter "${ANDROID_COMPONENTS}"
; \  
echo y | android update sdk --no-ui --all --filter "${GOOGLE_COMPONENTS}"  
ENV PATH $PATH:${ANDROID_HOME}/platform-tools  
  
# Install android ndk  
# ENV ANDROID_NDK_VER 11  
# RUN cd / && wget -q http://dl.google.com/android/repository/android-
ndk-r${ANDROID_NDK_VER}-linux-x86_64.zip  
# RUN unzip android-ndk-r${ANDROID_NDK_VER}-linux-x86_64.zip \  
# && mv android-ndk-r${ANDROID_NDK_VER}-linux-x86_64.tar.bz2
/usr/local/android-ndk-linux-r${ANDROID_NDK_VER} \  
# && rm -rf /android-ndk-r${ANDROID_NDK_VER}-linux-x86_64.zip \  
# && rm -rf /android-ndk-r${ANDROID_NDK_VER}-linux-x86_64.tar.bz2  
# ENV ANDROID_NDK_HOME /usr/local/android-ndk-linux-${ANDROID_NDK_VER}  
# ENV PATH $PATH:${ANDROID_NDK_HOME}  

