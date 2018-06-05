#  
# Android SDK Dockerfile  
#  
# https://github.com/uphyca/dockerfiles/android  
#  
  
FROM debian:jessie  
  
  
MAINTAINER Sosuke Masui "masui@uphyca.com"  
  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
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
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys EEA14886
&& \  
dpkg \--add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y \--force-yes \--no-install-recommends
$ANDROID_SDK_DEPENDENCIES oracle-java8-installer oracle-java8-set-default && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
/var/cache/oracle-jdk8-installer  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Install Gradle.  
RUN echo "deb http://ppa.launchpad.net/cwchien/gradle/ubuntu trusty main" |
tee /etc/apt/sources.list.d/cwchien-gradle.list && \  
echo "deb-src http://ppa.launchpad.net/cwchien/gradle/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/cwchien-gradle.list && \  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys EEA14886
&& \  
apt-get update -y && \  
apt-get install -y \--force-yes \--no-install-recommends gradle-2.14 && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
ENV GRADLE_HOME=/usr/lib/gradle/2.14/ \  
TERM=dumb  
  
  
# Install Android SDK.  
ENV ANDROID_SDK_URL=http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz
\  
ANDROID_HOME=/opt/android-sdk-linux \  
ANDROID_SDK=/opt/android-sdk-linux  
RUN apt-get update -y && \  
apt-get install -y \--force-yes \--no-install-recommends curl expect && \  
curl -L ${ANDROID_SDK_URL} | tar \--no-same-owner -xz -C /opt && \  
apt-get autoremove -y \--purge curl && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
ENV PATH $ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH  
  
  
# Install Android packages.  
COPY tools /opt/tools  
ENV PATH ${PATH}:/opt/tools  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk --no-ui
--all --filter platform-tools,build-tools-24.0.1,build-
tools-23.0.2,android-24,android-23,extra-android-m2repository,extra-
google-m2repository"]  
  
  
ENV DEBIAN_FRONTEND dialog  

