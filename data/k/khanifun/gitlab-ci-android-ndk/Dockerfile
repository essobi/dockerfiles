FROM khanifun/gitlab-ci-android  
MAINTAINER knizar <knizar@binar.co.id>  
  
ENV VERSION_ANDROID_NDK "android-ndk-r16b"  
ENV ANDROID_NDK_HOME "/sdk/${VERSION_ANDROID_NDK}"  
RUN apt-get -qq update && \  
apt-get install -qqy --no-install-recommends \  
build-essential \  
file \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD
https://dl.google.com/android/repository/${VERSION_ANDROID_NDK}-linux-x86_64.zip
/ndk.zip  
RUN unzip /ndk.zip -d /sdk && \  
rm -v /ndk.zip  

