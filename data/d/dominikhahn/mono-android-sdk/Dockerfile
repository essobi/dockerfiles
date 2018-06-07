# Pull base image.  
FROM mono:latest  
  
MAINTAINER Dominik Hahn <dominik@monostream.com>  
  
# Set ENV  
ENV DEBIAN_FRONTEND noninteractive  
ENV ANDROID_SDK_VERSION r24.4.1  
ENV ANDROID_BUILD_TOOLS_VERSION build-tools-15,build-tools-16,build-
tools-17,build-tools-18,build-tools-19,build-tools-20,build-tools-21,build-
tools-22,build-tools-23,build-tools-24  
ENV ANDROID_SDK_FILENAME android-sdk_${ANDROID_SDK_VERSION}-linux.tgz  
ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}  
ENV ANDROID_API_LEVELS
android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,android-24  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Add the WebUpd8 Oracle Java PPA repository for OpenJDK8 and enable gradle
daemon  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| debconf-set-selections && \  
mkdir -p ~/.gradle/ && \  
touch ~/.gradle/gradle.properties && \  
echo "org.gradle.daemon=true" >> ~/.gradle/gradle.properties  
  
# Enable multiarch i386, install OpenJDK, ADB & AAPT  
RUN dpkg --add-architecture i386 && \  
apt-get -yqq update && \  
apt-get -yqq --no-install-recommends install oracle-java8-installer libc6:i386
libncurses5:i386 libstdc++6:i386 lib32z1 && \  
apt-get -yqq autoremove && \  
apt-get -yqq clean && \  
rm -rf /var/lib/apt/lists/* /var/cache/* /tmp/* /var/tmp/*  
  
# Installs Android SDK and accept licenses  
RUN cd /opt && \  
curl -s ${ANDROID_SDK_URL} | tar -xz && \  
( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | android -s --clear-
cache update sdk --no-ui --force --all --filter tools,platform-
tools,${ANDROID_BUILD_TOOLS_VERSION},extra-android-
support,${ANDROID_API_LEVELS},extra-android-m2repository,extra-
google-m2repository && \  
mkdir -p "$ANDROID_HOME/licenses" && \  
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license" && \  
echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"$ANDROID_HOME/licenses/android-sdk-preview-license"  

