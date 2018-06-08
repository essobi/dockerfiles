FROM protopilotfactory/node:latest  
MAINTAINER Niek Palm <dev.npalm@gmail.com>  
  
ENV LANG en_US.UTF-8  
# add brightbox's repo, for ruby2.2  
# install python-software-properties (so you can do add-apt-repository)  
# install ruby2.2  
# install compass  
RUN apt-add-repository ppa:brightbox/ruby-ng && \  
apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-
properties software-properties-common && \  
apt-get -y install ruby2.2 ruby2.2-dev bundler javascript-common && \  
gem install compass  
  
# Android SDK is i386 only  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 wget
default-jdk && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
ENV ANDROID_SDK_VERSION 24.4.1  
RUN curl -SL http://dl.google.com/android/android-sdk_r$ANDROID_SDK_VERSION-
linux.tgz \  
| tar xz -C /opt  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
ENV ANDROID_API_LEVEL android-23  
ENV ANDROID_BUILD_TOOLS_VERSION 23.0.1  
RUN echo y | android update sdk --no-ui --all --filter platform-tools,build-
tools-${ANDROID_BUILD_TOOLS_VERSION},android-${android-23},extra-
android-m2repository,extra-google-m2repository  
  
RUN npm install cordova@6.0.0 -g

