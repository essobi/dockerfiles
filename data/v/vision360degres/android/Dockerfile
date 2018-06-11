FROM ubuntu:16.04  
MAINTAINER Martial Maillot "martial.maillot@gmail.com"  
ENV ANDROID_TOOLS_VERSION=3859397  
ENV ANDROID_API_LEVEL=27  
ENV ANDROID_BUILD_TOOLS_VERSION=27.0.3  
# Install required tools  
RUN apt-get update -qq  
  
# Dependencies to execute Android builds  
RUN dpkg --add-architecture i386  
RUN apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y expect git python curl
wget sudo unzip zip openjdk-8-jdk libc6:i386 libstdc++6:i386 libgcc1:i386
libncurses5:i386 libz1:i386  
RUN rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup environment  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
# Install Android SDK  
RUN cd /opt \  
&& wget -q https://dl.google.com/android/repository/sdk-tools-
linux-$ANDROID_TOOLS_VERSION.zip -O android-sdk-tools.zip \  
&& unzip -q android-sdk-tools.zip -d ${ANDROID_HOME} \  
&& rm -f android-sdk-tools.zip \  
&& chmod -R 777 ${ANDROID_HOME}  
  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
# Accept "android-sdk-license" before installing components, no need to echo y
for each component  
# License is valid for all the standard components in versions installed from
this file  
# Non-standard components: MIPS system images, preview versions, GDK (Google
Glass) and Android Google TV require separate licenses, not accepted there  
# RUN mkdir -p ${ANDROID_HOME}/licenses  
# RUN echo -e
"8933bad161af4178b1185d1a37fbf41ea5269c55\n\nd56f5187479451eabf01fb78af6dfcb131a6481e"
> ${ANDROID_HOME}/licenses/android-sdk-license  
# RUN yes | sdkmanager --licenses  
RUN mkdir ~/.android && echo '### User Sources for Android SDK Manager' >
~/.android/repositories.cfg  
  
RUN yes | sdkmanager --licenses && sdkmanager --update  
  
# Platform tools  
RUN sdkmanager "platform-tools"  
  
# SDK  
RUN sdkmanager "platforms;android-$ANDROID_API_LEVEL"  
  
# build tools  
RUN sdkmanager "build-tools;$ANDROID_BUILD_TOOLS_VERSION"  
  
# Extras  
RUN sdkmanager "extras;android;m2repository"  
RUN sdkmanager "extras;google;m2repository"  
RUN sdkmanager "extras;google;google_play_services"  
  
# If you want to chekc if packages has been installed or list all packages  
# RUN sdkmanager --list  
# Cleaning  
RUN apt-get clean  
  
# Go to workspace  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace  

