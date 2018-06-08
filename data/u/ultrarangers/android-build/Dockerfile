FROM openjdk:8  
  
MAINTAINER Lee Alexis  
  
# PARAMETERS  
###############################################################################  
  
# Noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
# ALT 1 : Version refers to commandline tools (sdkmanager)  
ENV ANDROID_CMD_TOOLS_VERSION 3859397  
ENV ANDROID_CMD_TOOLS_URL https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_CMD_TOOLS_VERSION}.zip  
  
ENV ANDROID_API_VERSION 27  
ENV ANDROID_BUILD_TOOLS_VERSION 27.0.3  
  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV ANDROID_SDK /usr/local/android-sdk-linux  
ENV ANDROID_NDK_HOME ${ANDROID_SDK}/ndk-bundle  
  
ENV PATH
$ANDROID_HOME/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:$ANDROID_HOME/platform-
tools:${ANDROID_NDK_HOME}$PATH  
  
# DOWNLOAD REQUESTS  
###############################################################################  
  
# Install dependencies  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -yq libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386
unzip wget build-essential rsync --no-install-recommends && \  
apt-get clean  
  
# SDK Tools from https://developer.android.com/studio/index.html  
RUN wget -q -O sdk-tools.zip "${ANDROID_CMD_TOOLS_URL}" \--no-check-
certificate && \  
mkdir -p $ANDROID_HOME && \  
unzip -q sdk-tools.zip && \  
mv tools $ANDROID_HOME && \  
rm -f sdk-tools.zip  
  
# INSTALLATIONS  
##############################################################################  
  
# Confirms that we agreed on the Terms and Conditions of the SDK itself  
# (if we didn’t the build would fail, asking us to agree on those terms).  
RUN mkdir -p "${ANDROID_HOME}/licenses" || true && \  
echo -e "\n601085b94cd77f0b54ff86406957099ebe79c4d6" >
"${ANDROID_HOME}/licenses/android-googletv-license" && \  
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"${ANDROID_HOME}/licenses/android-sdk-license" && \  
echo -e "\nd56f5187479451eabf01fb78af6dfcb131a6481e" >
"${ANDROID_HOME}/licenses/android-sdk-license" && \  
echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"${ANDROID_HOME}/licenses/android-sdk-preview-license" && \  
echo -e "\n33b6a2b64607f11b759f320ef9dff4ae5c47d97a" >
"${ANDROID_HOME}/licenses/google-gdk-license" && \  
echo -e "\nd975f751698a77b662f1254ddbeed3901e976f5a" >
"${ANDROID_HOME}/licenses/intel-android-extra-license" && \  
echo -e "\ne9acab5b5fbb560a72cfaecce8946896ff6aab9d" >
"${ANDROID_HOME}/licenses/mips-android-sysimage-license"  
  
RUN echo "Terms and Conditions" && \  
echo y | $ANDROID_HOME/tools/bin/sdkmanager --licenses  
  
# Install Android SDK components following our version  
RUN echo "Update Android SDK" && \  
echo y | sdkmanager --update --verbose && \  
echo "Install android-ANDROID_API_VERSION" && \  
echo y | sdkmanager "platform-tools"
"platforms;android-${ANDROID_API_VERSION}" \--verbose && \  
echo "Install build-tools-${ANDROID_BUILD_TOOLS_VERSION}" && \  
echo y | sdkmanager "build-tools;${ANDROID_BUILD_TOOLS_VERSION}" \--verbose &&
\  
echo "Install android-m2repository" && \  
echo y | sdkmanager "extras;android;m2repository" \--verbose && \  
echo "Install google-m2repository" && \  
echo y | sdkmanager "extras;google;m2repository" \--verbose && \  
echo "Install google_play_services" && \  
echo y | sdkmanager "extras;google;google_play_services" \--verbose && \  
echo "Install NDK with CMake, LLDB" && \  
echo y | sdkmanager "ndk-bundle" "lldb;3.1" "cmake;3.6.4111459"  
  
  
# POST-INSTALLATION  
##############################################################################  
  
# Cleanup  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/tmp* /tmp/*  
  
# Support Gradle  
ENV TERM dumb  
ENV JAVA_OPTS "-Xms512m -Xmx1024m"  
ENV GRADLE_OPTS "-XX:+UseG1GC -XX:MaxGCPauseMillis=1000"  
  
RUN echo "Installed."  

