FROM ubuntu:14.04  
MAINTAINER Alex Scherb "alexs@tablelist.com"  
# Install java8  
RUN apt-get update  
RUN apt-get install software-properties-common -y  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install oracle-java8-installer -y  
  
# Install Deps  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
--force-yes expect git wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5
lib32z1 python curl  
  
# Install Android SDK  
RUN cd /opt && wget --output-document=android-sdk.tgz --quiet
http://dl.google.com/android/android-sdk_r24.3.3-linux.tgz && tar xzf android-
sdk.tgz && rm -f android-sdk.tgz && chown -R root.root android-sdk-linux  
  
# Setup environment  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Install sdk elements  
ENV ANDROID_TOOLS platform-tools,build-tools-23.0.2  
ENV ANDROID_LEVELS android-18,android-22,android-23  
ENV ANDROID_GOOGLE_APIS addon-google_apis_x86-google-22,addon-
google_apis_x86-google-23  
ENV ANDROID_EXTRAS extra-android-support,extra-android-m2repository,extra-
google-m2repository,extra-google-google_play_services  
ENV ANDROID_SYS_IMG sys-img-armeabi-v7a-android-18  
RUN echo y | android update sdk --no-ui --all --filter
"${ANDROID_TOOLS},${ANDROID_LEVELS},${ANDROID_GOOGLE_APIS},${ANDROID_EXTRAS},${ANDROID_SYS_IMG}"  
  
RUN which adb  
RUN which android  
RUN android list targets  
  
# Create emulator  
RUN echo "no" | android create avd \  
\--force \  
\--device "Nexus 5" \  
\--name test \  
\--target android-18 \  
\--abi armeabi-v7a \  
\--skin WVGA800 \  
\--sdcard 512M  
  
# Add emulator scripts  
ADD wait-for-emulator ${ANDROID_HOME}/tools/  
ADD start-emulator ${ANDROID_HOME}/tools/  
RUN chmod 755 ${ANDROID_HOME}/tools/wait-for-emulator  
RUN chmod 755 ${ANDROID_HOME}/tools/start-emulator  
  
# Cleaning  
RUN apt-get clean  
  
# GO to workspace  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace  

