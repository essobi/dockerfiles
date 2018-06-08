FROM ubuntu:16.04  
  
# Installs Android SDK NDK  
ENV ANDROID_SDK_FILENAME android-sdk_r24.4.1-linux.tgz  
ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}  
  
ENV ANDROID_NDK_FILE android-ndk-r12b-linux-x86_64.zip  
ENV ANDROID_NDK_URL
https://dl.google.com/android/repository/${ANDROID_NDK_FILE}  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
ENV ANDROID_NDK_HOME /opt/android-ndk-r12b  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y wget curl unzip make libc6:i386 libncurses5:i386
libstdc++6:i386 lib32z1 && \  
apt-get install -y openjdk-8-jdk && \  
(curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash) && \  
apt-get install -y git-lfs=1.4.3 && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
RUN cd /opt && \  
wget ${ANDROID_SDK_URL} && tar -xzf ${ANDROID_SDK_FILENAME} && rm
${ANDROID_SDK_FILENAME} && \  
wget ${ANDROID_NDK_URL} && unzip ${ANDROID_NDK_FILE} && rm ${ANDROID_NDK_FILE}
&& \  
(echo "y" | android update sdk --no-ui --all \--filter tools) && \  
(echo "y" | android update sdk --no-ui --all \--filter platform-tools) && \  
(echo "y" | android update sdk --no-ui --all \--filter build-tools-25.0.2) &&
\  
(echo "y" | android update sdk --no-ui --all \--filter android-25) && \  
(echo "y" | android update sdk --no-ui --all \--filter extra-
android-m2repository) && \  
rm -rf \  
${ANDROID_NDK_HOME}/platforms/android-9 \  
${ANDROID_NDK_HOME}/platforms/android-12 \  
${ANDROID_NDK_HOME}/platforms/android-13 \  
${ANDROID_NDK_HOME}/platforms/android-14 \  
${ANDROID_NDK_HOME}/platforms/android-15 \  
${ANDROID_NDK_HOME}/platforms/android-16 \  
${ANDROID_NDK_HOME}/platforms/android-17 \  
${ANDROID_NDK_HOME}/toolchains/llvm \  
${ANDROID_NDK_HOME}/platforms/mips*  
  
  

