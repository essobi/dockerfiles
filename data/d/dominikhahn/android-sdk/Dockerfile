# Pull base image.  
FROM debian:jessie  
  
MAINTAINER Dominik Hahn <dominik@monostream.com>  
  
# Set ENV  
ENV ANDROID_SDK_VERSION=r25.2.3  
ENV ANDROID_BUILD_TOOLS_VERSION=build-tools-15,build-tools-16,build-
tools-17,build-tools-18,build-tools-19,build-tools-20,build-tools-21,build-
tools-22,build-tools-23,build-tools-24,build-tools-25  
ENV ANDROID_SDK_FILENAME=tools_${ANDROID_SDK_VERSION}-linux.zip  
ENV
ANDROID_SDK_URL=https://dl.google.com/android/repository/${ANDROID_SDK_FILENAME}  
ENV
ANDROID_API_LEVELS=android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,android-24,android-25  
ENV ANDROID_HOME=/opt/tools  
ENV PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Add OpenJDK8 and enable gradle daemon  
RUN echo "deb http://http.debian.net/debian jessie-backports main" | tee -a
/etc/apt/sources.list && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| debconf-set-selections && \  
mkdir -p ~/.gradle/ && \  
touch ~/.gradle/gradle.properties && \  
echo "org.gradle.daemon=true" >> ~/.gradle/gradle.properties  
  
# Enable multiarch i386, install OpenJDK, ADB & AAPT  
RUN dpkg --add-architecture i386 && \  
apt-get -yqq update && \  
apt-get -yqq install -t jessie-backports openjdk-8-jre ca-certificates-java &&
\  
apt-get -yqq install build-essential curl libc6:i386 libc6-dev:i386
libncurses5:i386 libstdc++6:i386 lib32z1 unzip && \  
update-alternatives --config java && \  
apt-get -yqq autoremove && \  
apt-get -yqq clean && \  
rm -rf /var/lib/apt/lists/* /var/cache/* /tmp/*  
  
# Installs Android SDK and accept licenses  
RUN cd /opt && \  
curl -sSO ${ANDROID_SDK_URL} && \  
unzip -q ${ANDROID_SDK_FILENAME} && \  
rm -rf ${ANDROID_SDK_FILENAME} && \  
( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | ${ANDROID_HOME}/android
-s --clear-cache update sdk --no-ui --force --all --filter tools,platform-
tools,${ANDROID_BUILD_TOOLS_VERSION},extra-android-
support,${ANDROID_API_LEVELS},extra-android-m2repository,extra-
google-m2repository && \  
mkdir -p "$ANDROID_HOME/licenses" && \  
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license" && \  
echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"$ANDROID_HOME/licenses/android-sdk-preview-license"

