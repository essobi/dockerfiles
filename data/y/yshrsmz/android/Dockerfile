FROM openjdk:8-jdk  
  
# https://github.com/bitrise-docker/android/blob/master/Dockerfile  
# https://github.com/bitrise-steplib/steps-start-android-
emulator/blob/master/step.rb  
  
LABEL maintainer "Shimizu Yasuhiro <the.phantom.bane+github@gmail.com>"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg --add-architecture i386 && \  
apt-get update -qq && \  
apt-get install -yq \  
git \  
curl \  
wget \  
rsync \  
sudo \  
expect \  
zip \  
unzip \  
file \  
build-essential \  
libc6:i386 \  
libstdc++6:i386 \  
libgcc1:i386 \  
libncurses5:i386 \  
libz1:i386 && \  
apt-get clean  
  
RUN mkdir /opt/bin && \  
curl -L
https://github.com/haya14busa/reviewdog/releases/download/0.9.8/reviewdog_linux_amd64
-o /opt/bin/reviewdog && \  
chmod 777 /opt/bin/reviewdog  
  
# Download and unzip SDK  
ENV ANDROID_HOME /opt/android-sdk-linux  
RUN mkdir /opt/android-sdk-linux && \  
cd /opt/android-sdk-linux && \  
wget -q https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
-O /opt/android-sdk-linux/tools.zip && \  
unzip tools.zip && \  
rm -f tools.zip  
  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools:/opt/bin  
  
# ------------------------------------------------------  
# --- Install Android SDKs and other build packages  
RUN echo y | sdkmanager \  
"platform-tools" \  
"build-tools;27.0.3" \  
"platforms;android-27" \  
"extras;android;m2repository" \  
"extras;google;m2repository"  
# Support Gradle  
ENV TERM dumb  

