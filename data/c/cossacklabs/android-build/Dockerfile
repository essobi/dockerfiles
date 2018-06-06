FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends sudo wget curl unzip git \  
build-essential ninja-build default-jdk && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Golang  
RUN wget -O /go.tar.gz \  
https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf /go.tar.gz && \  
rm /go.tar.gz  
ENV PATH=$PATH:/usr/local/go/bin  
  
RUN useradd \--groups sudo \--create-home \--shell /bin/bash user && \  
echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
mkdir /projects && chown user:user /projects  
USER user  
  
# Android SDK and NDK  
RUN wget -O ~/sdk-tools-linux.zip \  
https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \  
mkdir ~/android-sdk && \  
cd ~/android-sdk && \  
unzip ~/sdk-tools-linux.zip && \  
rm ~/sdk-tools-linux.zip && \  
yes | ~/android-sdk/tools/bin/sdkmanager \--licenses && \  
~/android-sdk/tools/bin/sdkmanager \--update && \  
~/android-sdk/tools/bin/sdkmanager 'build-tools;27.0.3' 'platforms;android-27'
'ndk-bundle' 'emulator'  
  
ENV ANDROID_HOME=/home/user/android-sdk  
# CMake  
RUN wget -O ~/cmake.sh \  
https://cmake.org/files/v3.10/cmake-3.10.1-Linux-x86_64.sh && \  
chmod u+x ~/cmake.sh && \  
mkdir ~/cmake && \  
~/cmake.sh \--skip-license \--prefix=/home/user/cmake && \  
rm ~/cmake.sh  
  
ENV PATH=/home/user/cmake/bin:$PATH  
  
WORKDIR /projects  

