FROM debian:unstable  
  
MAINTAINER Darren M. OConnell "doconnell@cursived.com"  
# Install java8  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
(echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections) && \  
apt-get update && \  
apt-get install -y --allow-unauthenticated oracle-java8-installer && \  
apt-get clean && \  
rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Deps  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
--force-yes --allow-unauthenticated expect git wget unzip zip libc6-i386
lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 python curl libqt5widgets5 &&
apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV
ANDROID_SDK_URL="https://dl.google.com/android/repository/tools_r25.2.3-linux.zip"
\  
ANDROID_BUILD_TOOLS_VERSION=25.0.2 \  
ANDROID_APIS="android-10,android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,android-24,android-25"
\  
ANT_HOME="/usr/share/ant" \  
MAVEN_HOME="/usr/share/maven" \  
GRADLE_HOME="/usr/share/gradle" \  
ANDROID_HOME="android"  
# Copy install tools  
COPY tools /opt/tools  
ENV PATH ${PATH}:/opt/tools  
  
# Installs Android SDK  
RUN mkdir android && cd android && \  
wget -O tools.zip ${ANDROID_SDK_URL} && \  
unzip tools.zip && rm tools.zip && cd tools &&\  
echo y | ./android update sdk -a -u -t platform-tools,${ANDROID_APIS},build-
tools-${ANDROID_BUILD_TOOLS_VERSION} && \  
chmod a+x -R ../tools && \  
chown -R root:root ../tools  
  
# Setup environment  
RUN mkdir "/android/tools/licenses" && echo -e
"\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"/android/tools/licenses/android-sdk-license"  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
RUN which adb  
RUN which android  
  
# Cleaning  
RUN apt-get clean  
  
# GO to workspace  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace  

