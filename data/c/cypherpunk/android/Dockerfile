#  
# Android SDK Dockerfile  
#  
FROM debian:jessie  
  
  
MAINTAINER Satoshi "satoshi@cypherpunk.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
# install common deps  
RUN apt-get update -y && apt-get install -y --force-yes --no-install-
recommends \  
curl \  
expect \  
ca-certificates \  
lsb-release \  
apt-transport-https \  
unzip  
  
# Install Oracle Java8.  
# http://www.webupd8.org/2014/03/how-to-install-oracle-java-8-in-debian.html  
#
https://developer.android.com/intl/ja/sdk/installing/index.html?pkg=tools#UbuntuTrouble  
# http://stackoverflow.com/questions/2710499/android-sdk-on-a-64-bit-linux-
machine  
ENV ANDROID_SDK_DEPENDENCIES "libc6 libstdc++6 zlib1g libncurses5"  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y --force-yes --no-install-recommends
$ANDROID_SDK_DEPENDENCIES oracle-java8-installer oracle-java8-set-default && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
/var/cache/oracle-jdk8-installer  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
  
# Install Gradle.  
RUN echo "deb http://ppa.launchpad.net/cwchien/gradle/ubuntu trusty main" |
tee /etc/apt/sources.list.d/cwchien-gradle.list && \  
echo "deb-src http://ppa.launchpad.net/cwchien/gradle/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/cwchien-gradle.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update -y && \  
apt-get install -y --force-yes --no-install-recommends gradle-3.3 && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
ENV GRADLE_HOME=/usr/lib/gradle/3.3/ \  
TERM=dumb  
  
  
# Install Android SDK.  
ENV ANDROID_SDK_URL=http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz
\  
ANDROID_HOME=/opt/android-sdk-linux \  
ANDROID_SDK=/opt/android-sdk-linux  
RUN curl -L ${ANDROID_SDK_URL} | tar --no-same-owner -xz -C /opt  
ENV PATH $ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH  
  
# Install new Android tools  
RUN rm -rf $ANDROID_HOME/tools  
RUN wget -q http://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip && \  
unzip sdk-tools-linux-3859397.zip -d $ANDROID_HOME  
  
# Install Android packages.  
RUN mkdir $ANDROID_HOME/licenses  
COPY licenses/android-sdk-license $ANDROID_HOME/licenses  
COPY tools /opt/tools  
ENV PATH ${PATH}:$ANDROID_HOME/tools/bin  
RUN sdkmanager --package_file=/opt/tools/package-file --verbose  
  
# Install Android NDK  
ENV ANDROID_NDK_VERSION=r12b  
RUN wget -q http://dl.google.com/android/repository/android-
ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip && \  
unzip android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip  
ENV ANDROID_NDK_HOME="${PWD}/android-ndk-${ANDROID_NDK_VERSION}"  
ENV PATH $PATH:${ANDROID_NDK_HOME}  
  
  
# Install Google Cloud SDK  
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - &&
\  
apt-get update -y && \  
apt-get install -y --force-yes --no-install-recommends google-cloud-sdk  
  
ENV DEBIAN_FRONTEND dialog  

