FROM cerebralfix/static-library-builder-base:latest  
  
MAINTAINER David Alexander <david@cerebralfix.com>  
  
WORKDIR /opt/ndk/  
  
RUN wget http://dl.google.com/android/ndk/android-ndk-r9-linux-x86_64.tar.bz2
-O ndk.tar.bz2  
RUN tar -xjvf ndk.tar.bz2  
  
ENV ANDROID_NDK /opt/ndk/android-ndk-r9/  

