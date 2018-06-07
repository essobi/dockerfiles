# Android development environment API-25 for ubuntu 16.04  
# version 0.0.1  
FROM ubuntu:16.04  
MAINTAINER Charles Liu <charles.liu@mioglobal.com>  
  
# Expose ADB, ADB control and VNC ports  
EXPOSE 5037  
EXPOSE 5554  
EXPOSE 5555  
# Update packages  
RUN apt-get update -qq \  
&& apt-get install -y wget openjdk-8-jdk unzip git libqt53dcollision5 net-
tools socat curl \  
&& apt-get clean  
  
# Install android sdk  
ARG ANDROID_SDK_VERSION=25.2.5  
RUN cd /opt && wget
https://dl.google.com/android/repository/tools_r${ANDROID_SDK_VERSION}-linux.zip
\  
&& unzip tools_r${ANDROID_SDK_VERSION}-linux.zip \  
&& rm -f tools_r${ANDROID_SDK_VERSION}-linux.zip \  
&& mkdir android-sdk && mv tools android-sdk/tools  
  
# Add android tools and platform tools to PATH  
ENV ANDROID_HOME /opt/android-sdk  
ENV PATH ${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${PATH}  
  
# Install latest android tools and system images  
RUN echo y | android update sdk -u -a -t platform-tools \  
&& echo y | android update sdk -u -a -t build-tools-25.0.2 \  
&& echo y | android update sdk -u -a -t android-25 \  
&& echo y | android update sdk -u -a -t extra-google-m2repository \  
&& echo y | android update sdk -u -a -t extra-android-m2repository \  
&& echo y | android update sdk -u -a -t sys-img-armeabi-v7a-google_apis-25  
  
# Create fake keymap file  
RUN mkdir /opt/android-sdk/tools/keymaps && \  
touch /opt/android-sdk/tools/keymaps/en-us  
  
# Add volume  
VOLUME /workspace  
WORKDIR /workspace  
  
# Add entrypoint  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

