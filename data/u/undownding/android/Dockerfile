FROM nimmis/ubuntu:14.04  
MAINTAINER UnDownDing <undownding@gmail.com>  
  
# Build-Variables  
ENV ANDROID_SDK_FILE android-sdk_r24.4.1-linux.tgz  
ENV ANDROID_SDK_URL https://dl.google.com/android/${ANDROID_SDK_FILE}  
ENV ANDROID_BUILD_TOOLS build-tools-23.0.2,build-tools-22.0.1  
ENV ANDROID_APIS android-22,android-23  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/  
  
# Set Environment Variables  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$_HOME/build-
tools/$ANDROID_BUILD_TOOLS_VERSION  
  
  
RUN add-apt-repository ppa:webupd8team/java -y && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get update && \  
apt-get install -y --no-install-recommends oracle-java8-installer && \  
apt-get install -y --no-install-recommends oracle-java8-set-default && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
RUN apt-get install -y curl expect \  
  
# install 32-bit dependencies require by the android sdk  
libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 \  
  
# install gradle  
gradle && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR "/opt"  
  
# Installs Android SDK  
RUN curl -O ${ANDROID_SDK_URL} && tar xf ${ANDROID_SDK_FILE} && \  
( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | android update sdk
--all --no-ui --filter platform-
tools,${ANDROID_APIS},${ANDROID_BUILD_TOOLS},extra-android-support,extra-
android-m2repository,extra-google-m2repository,extra-google-
google_play_services && \  
rm ${ANDROID_SDK_FILE}  
RUN ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | android update sdk
--all --no-ui --filter build-tools-24.0.1  

