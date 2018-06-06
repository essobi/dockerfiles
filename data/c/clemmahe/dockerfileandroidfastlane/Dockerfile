  
FROM openjdk:8  
  
MAINTAINER ClementMAHE <mahe.clem@gmail.com>  
  
ENV ANDROID_SDK_URL="https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip" \  
GRADLE_HOME="/usr/share/gradle" \  
ANDROID_HOME="/opt/android"  
  
ENV PATH
$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-
tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION:$GRADLE_HOME/bin  
  
WORKDIR /opt  
  
RUN dpkg --add-architecture i386 && \  
apt-get -qq update && \  
apt-get -qq install -y wget curl maven ant gradle libncurses5:i386
libstdc++6:i386 zlib1g:i386 && \  
# Installs Android SDK  
mkdir android && cd android && \  
wget -O tools.zip ${ANDROID_SDK_URL} && \  
unzip tools.zip && rm tools.zip && \  
# Copy licenses  
mkdir -p licenses && \  
echo 8933bad161af4178b1185d1a37fbf41ea5269c55 > licenses/android-sdk-license
&& \  
echo 84831b9409646a918e30573bab4c9c91346d8abd > licenses/android-sdk-preview-
license && \  
# Install  
echo "Installing apk..." && \  
sdkmanager "platforms;android-25" \  
"platforms;android-26" \  
"build-tools;25.0.3" \  
"build-tools;26.0.0" \  
"extras;google;google_play_services" \  
"extras;google;m2repository" \  
"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.1" \  
"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2" \  
"system-images;android-25;google_apis;x86" \  
"emulator" \--verbose && \  
# Install package emulator dependencies  
echo "Install emulator dependencies" && \  
#Update & install https transport  
echo y | apt-get update && apt-get install -y apt-transport-https && \  
#Install dependencies  
# Clean up  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && \  
apt-get clean \  

