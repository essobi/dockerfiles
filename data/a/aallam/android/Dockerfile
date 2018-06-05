FROM aallam/oracle-java:8  
MAINTAINER aallam  
  
ARG ANDROID_COMPILE_SDK=27  
ARG ANDROID_BUILD_TOOLS=27.0.3  
ARG ANDROID_SDK_TOOLS=3859397  
ARG
ANDROID_SDK_TOOLS_SHA256=444e22ce8ca0f67353bda4b85175ed3731cae3ffa695ca18119cbacef1c1bea0  
  
ENV ANDROID_HOME /opt/android/sdk  
ENV PATH="${PATH}:${ANDROID_HOME}/platform-tools"  
RUN apt-get --quiet update --yes && apt-get --quiet install --yes wget unzip
&& \  
wget --quiet --output-document=/tmp/sdk-tools-linux.zip
https://dl.google.com/android/repository/sdk-tools-
linux-$ANDROID_SDK_TOOLS.zip && \  
echo "$ANDROID_SDK_TOOLS_SHA256 /tmp/sdk-tools-linux.zip" | sha256sum -c - &&
\  
mkdir -p $ANDROID_HOME && unzip -q /tmp/sdk-tools-linux.zip -d $ANDROID_HOME
&& \  
rm /tmp/sdk-tools-linux.zip  
  
RUN apt-get --quiet update --yes && apt-get --quiet install --yes lib32stdc++6
lib32z1 && \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager
"platforms;android-$ANDROID_COMPILE_SDK" "build-tools;$ANDROID_BUILD_TOOLS"
"extras;google;m2repository" "extras;android;m2repository"
"extras;google;google_play_services"  

