FROM ubuntu:14.04  
MAINTAINER jsonfry "jason@ocasta.com"  
# Install Java  
RUN DEBIAN_FRONTEND=noninteractive \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
>> /etc/apt/sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 \  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get install -y --no-install-recommends oracle-java8-installer
lib32ncurses5 lib32stdc++6 lib32z1 unzip \  
&& apt-get clean  
  
# Download And Extract Android SDK  
WORKDIR /opt/android-sdk  
RUN wget -nv http://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip \  
&& unzip sdk-tools-linux-3859397.zip \  
&& rm -f sdk-tools-linux-3859397.zip  
  
# Android SDK Paths  
ENV ANDROID_HOME /opt/android-sdk  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
RUN mkdir -p ${ANDROID_HOME}/licenses  
RUN echo d56f5187479451eabf01fb78af6dfcb131a6481e >
${ANDROID_HOME}/licenses/android-sdk-license  
  
# Android packages  
ADD packages /opt/android-sdk/packages  
RUN sdkmanager --package_file=packages  
  
# ADB Key - Be careful what you do with devices that trust the built in key  
ADD adbkey /root/.android/adbkey  
ADD adbkey.pub /root/.android/adbkey.pub  

