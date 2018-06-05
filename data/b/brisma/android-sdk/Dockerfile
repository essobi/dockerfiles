FROM ubuntu:16.04  
  
MAINTAINER Manuel Valentino <brisma@gmail.com>  
  
ENV ANDROID_HOME /opt/android-sdk  
ENV ANDROID_NDK /opt/android-ndk  
ENV ANDROID_NDK_HOME /opt/android-ndk  
  
# Get the latest version from https://developer.android.com/studio/index.html  
ENV ANDROID_SDK_VERSION="3859397"  
# Get the latest version from
https://developer.android.com/ndk/downloads/index.html  
ENV ANDROID_NDK_VERSION="14b"  
  
WORKDIR /tmp  
  
# Installing packages  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
autoconf \  
git \  
curl \  
wget \  
lib32stdc++6 \  
lib32z1 \  
lib32z1-dev \  
lib32ncurses5 \  
libc6-dev \  
libgmp-dev \  
libmpc-dev \  
libmpfr-dev \  
libxslt-dev \  
libxml2-dev \  
m4 \  
ncurses-dev \  
ocaml \  
openssh-client \  
pkg-config \  
python-software-properties \  
software-properties-common \  
unzip \  
zip \  
zlib1g-dev && \  
apt-add-repository -y ppa:openjdk-r/ppa && \  
apt-get install -y openjdk-8-jdk && \  
rm -rf /var/lib/apt/lists/ && \  
apt-get clean  
  
# Install Android SDK  
RUN wget -q -O tools.zip https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_VERSION}.zip && \  
unzip -q tools.zip && \  
rm -fr $ANDROID_HOME tools.zip && \  
mkdir -p $ANDROID_HOME && \  
mv tools $ANDROID_HOME/tools && \  
  
mkdir -p $ANDROID_HOME/licenses && \  
echo 8933bad161af4178b1185d1a37fbf41ea5269c55 >
$ANDROID_HOME/licenses/android-sdk-license && \  
echo 84831b9409646a918e30573bab4c9c91346d8abd >
$ANDROID_HOME/licenses/android-sdk-preview-license && \  
# Install Android components  
cd $ANDROID_HOME && \  
  
echo "Install Google API 15" && \  
tools/bin/sdkmanager "add-ons;addon-google_apis-google-15" && \  
echo "Install Google API 16" && \  
tools/bin/sdkmanager "add-ons;addon-google_apis-google-16" && \  
echo "Install Google API 17" && \  
tools/bin/sdkmanager "add-ons;addon-google_apis-google-17" && \  
echo "Install Google API 18" && \  
tools/bin/sdkmanager "add-ons;addon-google_apis-google-18" && \  
echo "Install Google API 19" && \  
tools/bin/sdkmanager "add-ons;addon-google_apis-google-19" && \  
echo "Install Google API 21" && \  
tools/bin/sdkmanager "add-ons;addon-google_apis-google-21" && \  
echo "Install Google API 22" && \  
tools/bin/sdkmanager "add-ons;addon-google_apis-google-22" && \  
echo "Install Google API 23" && \  
tools/bin/sdkmanager "add-ons;addon-google_apis-google-23" && \  
echo "Install Google API 24" && \  
tools/bin/sdkmanager "add-ons;addon-google_apis-google-24" && \  
  
echo "Install android-16" && \  
tools/bin/sdkmanager "platforms;android-16" && \  
echo "Install android-17" && \  
tools/bin/sdkmanager "platforms;android-17" && \  
echo "Install android-18" && \  
tools/bin/sdkmanager "platforms;android-18" && \  
echo "Install android-19" && \  
tools/bin/sdkmanager "platforms;android-19" && \  
echo "Install android-20" && \  
tools/bin/sdkmanager "platforms;android-20" && \  
echo "Install android-21" && \  
tools/bin/sdkmanager "platforms;android-21" && \  
echo "Install android-22" && \  
tools/bin/sdkmanager "platforms;android-22" && \  
echo "Install android-23" && \  
tools/bin/sdkmanager "platforms;android-23" && \  
echo "Install android-24" && \  
tools/bin/sdkmanager "platforms;android-24" && \  
echo "Install android-25" && \  
tools/bin/sdkmanager "platforms;android-25" && \  
  
echo "Install platform-tools" && \  
tools/bin/sdkmanager "platform-tools" && \  
  
echo "Install build-tools-19.1.0" && \  
tools/bin/sdkmanager "build-tools;19.1.0" && \  
echo "Install build-tools-20.0.0" && \  
tools/bin/sdkmanager "build-tools;20.0.0" && \  
echo "Install build-tools-21.1.2" && \  
tools/bin/sdkmanager "build-tools;21.1.2" && \  
echo "Install build-tools-22.0.1" && \  
tools/bin/sdkmanager "build-tools;22.0.1" && \  
echo "Install build-tools-23.0.1" && \  
tools/bin/sdkmanager "build-tools;23.0.1" && \  
echo "Install build-tools-23.0.2" && \  
tools/bin/sdkmanager "build-tools;23.0.2" && \  
echo "Install build-tools-23.0.3" && \  
tools/bin/sdkmanager "build-tools;23.0.3" && \  
echo "Install build-tools-24.0.0" && \  
tools/bin/sdkmanager "build-tools;24.0.0" && \  
echo "Install build-tools-24.0.1" && \  
tools/bin/sdkmanager "build-tools;24.0.1" && \  
echo "Install build-tools-24.0.2" && \  
tools/bin/sdkmanager "build-tools;24.0.2" && \  
echo "Install build-tools-24.0.3" && \  
tools/bin/sdkmanager "build-tools;24.0.3" && \  
echo "Install build-tools-25.0.0" && \  
tools/bin/sdkmanager "build-tools;25.0.0" && \  
echo "Install build-tools-25.0.1" && \  
tools/bin/sdkmanager "build-tools;25.0.1" && \  
echo "Install build-tools-25.0.2" && \  
tools/bin/sdkmanager "build-tools;25.0.2" && \  
echo "Install build-tools-25.0.3" && \  
tools/bin/sdkmanager "build-tools;25.0.3" && \  
  
echo "Install extra-android-m2repository" && \  
tools/bin/sdkmanager "extras;android;m2repository" && \  
  
echo "Install extra-google-google_play_services" && \  
tools/bin/sdkmanager "extras;google;google_play_services" && \  
  
echo "Install extra-google-m2repository" && \  
tools/bin/sdkmanager "extras;google;m2repository" && \  
  
echo "Install CMake 3.6.3155560" && \  
tools/bin/sdkmanager "cmake;3.6.3155560" && \  
  
echo "Install Google Play APK Expansion library" && \  
tools/bin/sdkmanager "extras;google;market_apk_expansion" && \  
  
echo "Install Google Play Licensing Library" && \  
tools/bin/sdkmanager "extras;google;market_licensing" && \  
  
echo "Install Google Play Billing Library" && \  
tools/bin/sdkmanager "extras;google;play_billing" && \  
  
echo "Install SDK Patch Applier v4" && \  
tools/bin/sdkmanager "patcher;v4" && \  
  
echo "Install tools 26.0.2" && \  
tools/bin/sdkmanager "tools"  
# Install Android NDK, put it in a separate RUN to avoid travis-ci timeout in
10 minutes.  
RUN wget -q -O android-ndk.zip
http://dl.google.com/android/repository/android-
ndk-r${ANDROID_NDK_VERSION}-linux-x86_64.zip && \  
unzip -q android-ndk.zip && \  
rm -fr $ANDROID_NDK android-ndk.zip && \  
mv android-ndk-r${ANDROID_NDK_VERSION} $ANDROID_NDK  
  
# Add android commands to PATH  
ENV ANDROID_SDK_HOME $ANDROID_HOME  
ENV PATH $PATH:$ANDROID_SDK_HOME/tools:$ANDROID_SDK_HOME/platform-
tools:$ANDROID_NDK  
  
# Export JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
  
# Support Gradle  
ENV TERM dumb  
ENV JAVA_OPTS "-Xms512m -Xmx1536m"  
ENV GRADLE_OPTS "-XX:+UseG1GC -XX:MaxGCPauseMillis=1000"  
  
WORKDIR /project  

