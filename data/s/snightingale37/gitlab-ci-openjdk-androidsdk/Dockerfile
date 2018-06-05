#  
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY.  
#  
FROM ubuntu:16.04  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# Android specific constants  
ENV VERSION_SDK_TOOLS "3859397"  
ENV ANDROID_HOME "/sdk"  
ENV PATH "$PATH:${ANDROID_HOME}/tools"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update && \  
apt-get install -qqy --no-install-recommends \  
curl \  
html2text \  
openjdk-8-jdk \  
libc6-i386 \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
unzip \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN rm -f /etc/ssl/certs/java/cacerts; \  
/var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
# Setup the CI for Android builds  
RUN apt-get --quiet update --yes  
RUN apt-get --quiet install --yes wget tar unzip lib32stdc++6 lib32z1  
RUN wget --quiet --output-document=android-sdk.zip
https://dl.google.com/android/repository/tools_r25.2.5-linux.zip  
RUN unzip android-sdk.zip  
RUN echo y | tools/android --silent update sdk --no-ui --all --filter
android-25  
RUN echo y | tools/android --silent update sdk --no-ui --all --filter
platform-tools  
RUN echo y | tools/android --silent update sdk --no-ui --all --filter build-
tools-25.0.2  
RUN echo y | tools/android --silent update sdk --no-ui --all --filter extra-
android-m2repository  
RUN echo y | tools/android --silent update sdk --no-ui --all --filter extra-
google-google_play_services  
RUN echo y | tools/android --silent update sdk --no-ui --all --filter extra-
google-m2repository  
  
# Google related licensing  
RUN mkdir -p $ANDROID_HOME/licenses/ \  
&& echo "8933bad161af4178b1185d1a37fbf41ea5269c55" >
$ANDROID_HOME/licenses/android-sdk-license \  
&& echo "84831b9409646a918e30573bab4c9c91346d8abd" >
$ANDROID_HOME/licenses/android-sdk-preview-license

