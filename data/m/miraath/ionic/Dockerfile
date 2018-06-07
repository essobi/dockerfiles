FROM ubuntu:14.04.4  
MAINTAINER mirathdev [at] gmail [dot] com  
  
ENV DEBIAN_FRONTEND=noninteractive \  
ANDROID_HOME=/opt/android-sdk-linux \  
# Fix for the issue with Selenium, as described here:  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
DBUS_SESSION_BUS_ADDRESS=/dev/null  
  
# Install basics  
RUN apt-get update -qq && \  
apt-get install -qq -y git wget curl unzip ruby build-essential xvfb && \  
  
## Chrome  
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
&& \  
dpkg --unpack google-chrome-stable_current_amd64.deb && \  
apt-get install -f -qq -y && \  
apt-get clean && \  
rm google-chrome-stable_current_amd64.deb && \  
  
## Font libraries  
apt-get -qq -y install fonts-ipafont-gothic xfonts-100dpi xfonts-75dpi xfonts-
cyrillic xfonts-scalable ttf-ubuntu-font-family libfreetype6 libfontconfig  
  
# Node stuff  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -qq -y nodejs && \  
  
## Global packages  
npm install -g gulp-cli cordova ionic && \  
npm cache clean && \  
  
## Yarn (Node package manager)  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update -qq && \  
apt-get install -qq -y yarn && \  
mkdir -p /root/.cache/yarn/  
  
# Oracle Java 8  
## install python-software-properties (so you can do add-apt-repository)  
RUN apt-get install -qq -y python-software-properties software-properties-
common && \  
add-apt-repository ppa:webupd8team/java -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update -qq && \  
apt-get -qq -y install oracle-java8-installer  
  
# Android SDK  
RUN echo ANDROID_HOME="${ANDROID_HOME}" >> /etc/environment && \  
dpkg --add-architecture i386 && \  
apt-get install -qq -y \--force-yes expect ant wget libc6-i386 lib32stdc++6
lib32gcc1 lib32ncurses5 lib32z1 qemu-kvm kmod && \  
cd /opt && \  
wget --output-document=android-sdk.tgz --quiet
http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \  
tar xzf android-sdk.tgz && \  
rm -f android-sdk.tgz && \  
chown -R root. /opt  
  
## Setup environment  
ENV PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:/opt/tools  
  
## Install sdk elements  
COPY sh /opt/tools  
### (Get the list of packages names: `android list sdk -e -a`)  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk --all --no-
ui --filter platform-tools,tools,build-tools-25.0.2,android-24,sys-
img-x86_64-google_apis-24,addon-google_apis-google-24,extra-android-
support,extra-android-m2repository,extra-google-m2repository,extra-google-
google_play_services"]  
RUN unzip ${ANDROID_HOME}/temp/*.zip -d ${ANDROID_HOME} && \  
rm ${ANDROID_HOME}/temp/*.zip && \  
### This make accept the license, for `ionic build`  
mkdir $ANDROID_HOME/licenses && \  
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license"  
  
# Cleaning APT stuff  
RUN apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /project  
WORKDIR /project  
EXPOSE 8100 35729  
# CMD ["ionic", "serve"]  

