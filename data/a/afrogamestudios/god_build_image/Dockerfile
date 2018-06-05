FROM node:latest  
  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y libncurses5:i386 libc6:i386 libstdc++6:i386 lib32gcc1
lib32ncurses5 lib32z1 zlib1g:i386 && \  
apt-get install -y git wget zip && \  
apt-get install sudo &&\  
apt-get install -y --no-install-recommends apt-utils &&\  
sudo apt-get update &&\  
sudo apt-get install -y wine &&\  
sudo apt-get install -y wine-development  
  
# openjdk 8  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
unzip \  
xz-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'deb http://deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
ENV JAVA_VERSION 8u121  
ENV JAVA_DEBIAN_VERSION 8u121-b13-1~bpo8+1  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20161107~bpo8+1  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \  
&& rm -rf /var/lib/apt/lists/* \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
# download and install Gradle  
ENV GRADLE_VERSION 3.5  
RUN cd /opt && \  
wget -q
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip &&
\  
unzip gradle*.zip && \  
ls -d */ | sed 's/\/*$//g' | xargs -I{} mv {} gradle && \  
rm gradle*.zip  
  
# remove android apis to reduce image size  
ENV
ANDROID_SDK_URL="https://dl.google.com/android/repository/tools_r25.2.3-linux.zip"
\  
ANDROID_BUILD_TOOLS_VERSION=25.0.2 \  
ANDROID_APIS="android-10,android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,android-24,android-25"
\  
ANT_HOME="/usr/share/ant" \  
MAVEN_HOME="/usr/share/maven" \  
GRADLE_HOME="/opt/gradle" \  
ANDROID_HOME="/opt/android"  
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-
tools:$ANDROID_HOME/build-
tools/$ANDROID_BUILD_TOOLS_VERSION:$ANT_HOME/bin:$MAVEN_HOME/bin:$GRADLE_HOME/bin  
  
WORKDIR /opt  
  
RUN dpkg --add-architecture i386 && \  
apt-get -qq update && \  
apt-get -qq install -y wget curl maven ant && \  
  
# Installs Android SDK  
mkdir android && cd android && \  
wget -O tools.zip ${ANDROID_SDK_URL} && \  
unzip tools.zip && rm tools.zip && \  
echo y | android update sdk -a -u -t platform-tools,${ANDROID_APIS},build-
tools-${ANDROID_BUILD_TOOLS_VERSION} && \  
chmod a+x -R $ANDROID_HOME && \  
chown -R root:root $ANDROID_HOME  
  
# custom  
RUN sudo apt-get update -y && \  
apt-get install -y apt-transport-https &&\  
curl -L https://packagecloud.io/github/git-lfs/gpgkey | apt-key add \- &&\  
curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | sudo bash &&\  
apt-get install -y debian-archive-keyring git-lfs libxml2-utils &&\  
apt-get install -y lftp &&\  
sudo npm install cordova -g &&\  
npm install electron-packager -g &&\  
npm install uglify-js -g &&\  
npm install uglifyify -g &&\  
sudo apt-get update -y &&\  
apt-get -qq install git-ftp &&\  
npm install -g browserify &&\  
npm install -g babel-cli &&\  
sudo apt-get update -y &&\  
sudo apt-get install cpio &&\  
sudo apt-get install xsltproc &&\  
apt-get purge -y software-properties-common &&\  
rm -rf /var/lib/apt/lists/*  

