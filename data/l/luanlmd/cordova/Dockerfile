FROM ubuntu:xenial  
  
MAINTAINER Luan Almeida <luanlmd@gmail.com>  
  
RUN apt update  
RUN apt upgrade -y  
RUN apt install wget unzip xz-utils -y  
RUN apt clean  
  
RUN wget
http://download.java.net/java/jdk8u152/archive/b05/binaries/jdk-8u152-ea-
bin-b05-linux-x64-20_jun_2017.tar.gz -O smelly.tar.gz  
RUN tar -xvzf smelly.tar.gz -C /opt  
RUN rm smelly.tar.gz  
ENV JAVA_HOME /opt/jdk1.8.0_152  
  
RUN wget https://services.gradle.org/distributions/gradle-4.0.2-bin.zip -O
ouch.zip  
RUN unzip ouch.zip -d /opt/  
RUN rm ouch.zip  
ENV GRADLE_HOME /opt/gradle-4.0.2/bin  
  
RUN wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
-O sdk.zip  
RUN unzip sdk.zip -d /opt/android  
RUN rm sdk.zip  
ENV ANDROID_HOME /opt/android  
  
RUN wget https://nodejs.org/dist/v8.2.1/node-v8.2.1-linux-x64.tar.xz -O
node.tar.xz  
RUN tar xf node.tar.xz -C /opt/  
RUN rm node.tar.xz  
ENV NODE_HOME /opt/node-v8.2.1-linux-x64/bin  
  
ENV PATH
$PATH:$NODE_HOME:$JAVA_HOME:$GRADLE_HOME:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-
tools  
  
RUN echo y | sdkmanager "platform-tools"  
RUN echo y | sdkmanager "build-tools;26.0.1"  
RUN echo y | sdkmanager "platforms;android-25"  
RUN echo y | sdkmanager "platforms;android-26"  
  
RUN npm i cordova -g  
  
RUN cordova telemetry off  
  
RUN cordova create test  
RUN cd test && cordova platform add android && cordova build  
RUN rm -Rf test  
  
VOLUME /src  
WORKDIR /src  
  
CMD ["cordova"]  

