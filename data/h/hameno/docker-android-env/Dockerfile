FROM ubuntu:14.04  
  
MAINTAINER Philip Schiffer "admin@psdev.de"  
  
# no interaction for apt-get etc  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Install java8  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
(echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections) && \  
apt-get update && \  
apt-get install -y oracle-java8-installer oracle-java8-set-default oracle-
java8-unlimited-jce-policy && \  
apt-get clean && \  
rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Deps  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y \--force-yes expect git wget unzip libc6-i386 lib32stdc++6
lib32gcc1 lib32ncurses5 lib32z1 python curl libqt5widgets5 && \  
apt-get clean && \  
rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download & Extract SDK  
RUN mkdir -p /root/.android/ && touch /root/.android/repositories.cfg && \  
cd /opt && \  
echo "Downloading sdk tools 25.2.3..." && \  
wget --output-document=tools.zip --quiet
https://dl.google.com/android/repository/tools_r25.2.3-linux.zip && \  
mkdir /opt/android-sdk-linux && cd /opt/android-sdk-linux && \  
unzip ../tools.zip > /dev/null && \  
rm -f ../tools.zip  
  
# Install Android SDK  
RUN cd /opt/android-sdk-linux && \  
mkdir "licenses" && \  
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > licenses/android-sdk-
license && \  
echo -en "\nd23d63a1f23e25e2c7a316e29eb60396e7924281" > licenses/android-sdk-
preview-license && \  
chown -R root.root /opt/android-sdk-linux && \  
echo -n "Installing tools, platform-tools: " && tools/bin/sdkmanager "tools"
"platform-tools" && \  
echo -n "Installing build-tools 25.0.2: " && tools/bin/sdkmanager "build-
tools;25.0.2" "platforms;android-25" && \  
echo -n "Installing cmake: " && tools/bin/sdkmanager "cmake;3.6.3155560" && \  
echo -n "Installing m2repositories: " && tools/bin/sdkmanager
"extras;android;m2repository" "extras;google;m2repository" && \  
echo -n "Installing constraint-layout: " && tools/bin/sdkmanager
"extras;m2repository;com;android;support;constraint;constraint-
layout;1.0.0-beta4" && \  
echo -n "Installing constraint-layout-solver: " && tools/bin/sdkmanager
"extras;m2repository;com;android;support;constraint;constraint-layout-
solver;1.0.0-beta4" && \  
echo -n "Installing ndk: " && tools/bin/sdkmanager "ndk-bundle" && \  
echo -n "Updating everything: " && tools/bin/sdkmanager --update  
  
# Setup environment  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
RUN which adb && which android  
  
# GO to workspace  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace

