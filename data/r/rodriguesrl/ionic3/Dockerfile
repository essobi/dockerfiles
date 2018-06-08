FROM ubuntu:16.04  
  
MAINTAINER Raphael Rodrigues <raphael.rodrigues.lima@gmail.com>  
  
ENV IONIC_VERSION 3.4.0  
ENV ANDROID_HOME="/opt/android-sdk-linux/"  
ENV PATH=$PATH:$ANDROID_HOME/platform-
tools:$ANDROID_HOME/tools:$ANDROID_HOME/build-tools  
  
#Initial Setup and Ionic installation  
RUN apt-get update && apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs && npm install -g cordova@7.0.1 && \  
npm install -g ionic@${IONIC_VERSION}  
  
#Install Java  
RUN apt-get install -y software-properties-common && \  
apt-add-repository -y ppa:webupd8team/java && apt-get update && \  
yes | apt-get install -y oracle-java8-installer  
  
#Install Android SDK  
RUN cd /opt && wget http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz
&& \  
tar -xvf android-sdk*-linux.tgz && rm android-sdk_r24.4.1-linux.tgz && \  
cd /opt/android-sdk-linux/tools && echo y | ./android update sdk --no-ui --all
\--filter platform-tools,build-tools,android-25  
  
#Install SDKs Dependencies  
RUN android list sdk --all && echo y | android update sdk -u -t 1,2,4,26,103
&& \  
apt-get install -y zip && cd /opt/android-sdk-linux/ && \  
mv ./temp/tools_r25.2.5-linux.zip ./ && unzip tools_r25.2.5-linux.zip  
  
#Install Gradle  
RUN apt-get install -y gradle  
  
#Final Adjustments  
RUN apt-get install -y git && rm -r /tmp/ && mkdir /tmp/  
WORKDIR /tmp/  

