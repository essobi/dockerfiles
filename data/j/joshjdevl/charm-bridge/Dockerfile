from ubuntu:precise  
MAINTAINER joshjdevl < joshjdevl [at] gmail {dot} com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV NDK_ROOT /installs/android-ndk-r9c  
  
RUN apt-get update  
RUN apt-get install -y python-software-properties  
RUN apt-get update  
RUN apt-get install -y wget git  
RUN mkdir /installs  
RUN cd /installs && wget http://dl.google.com/android/ndk/android-
ndk-r9c-linux-x86_64.tar.bz2  
RUN apt-get install bzip2  
RUN cd /installs && tar -xvf android-ndk-r9c-linux-x86_64.tar.bz2  
RUN apt-get update  
RUN apt-get -y install autoconf autoconf automake build-essential  
  
ENV PATH /installs/android-toolchain/bin:${NDK_ROOT}:$PATH  
RUN apt-get install -y vim  
RUN ${NDK_ROOT}/build/tools/make-standalone-toolchain.sh --platform=android-14
--arch=arm --install-dir=/installs/android-toolchain --system=linux-x86_64
--ndk-dir=${NDK_ROOT}  
ENV PATH ${NDK_ROOT}:$PATH  
ENV ANDROID_NDK_HOME ${NDK_ROOT}  
RUN mkdir -p /installs/charm-crypto-bridge  
RUN cd /installs/charm-crypto-bridge && git clone
https://github.com/mhlakhani/charm-crypto  
RUN apt-get -y install mercurial  
RUN cd /installs && hg clone https://code.google.com/p/haggle/  
RUN cd /installs/charm-crypto-bridge/charm-crypto/ccb/ccb && git pull  
RUN cd /installs/charm-crypto-bridge/charm-crypto/ccb/ccb && make  

