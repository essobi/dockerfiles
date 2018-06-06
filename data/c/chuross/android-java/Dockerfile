FROM isuper/java-oracle:jdk_8  
  
MAINTAINER chuross <azarasi.mo.mo@gmail.com>  
  
RUN dpkg --add-architecture i386 \  
&& apt-get -yq update \  
&& apt-get -yq install libncurses5:i386 libstdc++6:i386 zlib1g:i386 --no-
install-recommends \  
&& apt-get clean  
  
# Android arguments  
ARG ANDROID_SDK_VERSION="24.4.1"  
ENV ANDROID_SDK_URL http://dl.google.com/android/android-
sdk_r${ANDROID_SDK_VERSION}-linux.tgz  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:$PATH  
  
# Android components  
ENV ANDROID_COMPONENTS platform-tools  
  
# install Android  
RUN curl -sL "${ANDROID_SDK_URL}" | tar xz --no-same-owner -C /usr/local  
RUN echo y | android update sdk --no-ui --all --filter "${ANDROID_COMPONENTS}"  

