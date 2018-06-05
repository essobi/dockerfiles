FROM frolvlad/alpine-oraclejdk8:latest  
MAINTAINER Audrius Karosevicius <audrius.karosevicius@gmail.com>  
  
ENV ANDROID_HOME=/opt/android-sdk  
  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache bash wget git unzip  
  
#Releases https://dl.google.com/android/repository/repository2-1.xml  
RUN SDK_BUILD="4333796"
SDK_CHECKSUM="8c7c28554a32318461802c1291d76fccfafde054" \  
&& wget -q https://dl.google.com/android/repository/sdk-tools-
linux-"$SDK_BUILD".zip \  
&& echo "$SDK_CHECKSUM *sdk-tools-linux-$SDK_BUILD.zip" | sha1sum -c - \  
&& mkdir /opt \  
&& unzip -qq sdk-tools-linux-"$SDK_BUILD".zip -d /opt/android-sdk \  
&& rm sdk-tools-linux-"$SDK_BUILD".zip \  
&& yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses \  
&& chmod -R 777 $ANDROID_HOME  
  

