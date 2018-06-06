FROM node:7.2.0  
# Ionic  
RUN \  
npm install -g \  
cordova \  
ionic \  
cordova-plugin-device \  
cordova-plugin-console \  
cordova-plugin-whitelist \  
cordova-plugin-splashscreen \  
cordova-plugin-statusbar \  
ionic-plugin-keyboard \  
cordova-android && \  
cordova-browser && \  
npm cache clean  
  
# Android SDK  
RUN \  
cd /opt && \  
curl https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz -o "android-
sdk.tgz" && \  
tar --no-same-owner -zxvf android-sdk.tgz && \  
rm -f android-sdk.tgz  
ENV ANDROID_HOME=/opt/android-sdk-linux  
  
# Java 8  
RUN \  
echo 'deb http://deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-get update && \  
apt-get install -y openjdk-8-jdk && \  
rm -rf /var/lib/apt/lists/*  

