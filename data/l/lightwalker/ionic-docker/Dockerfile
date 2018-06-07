FROM ubuntu:16.04  
MAINTAINER Kirill Gusyatin "kirill.gus@gmail.com"  
  
# Install apt packages  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y software-properties-common libncurses5:i386
libstdc++6:i386 zlib1g:i386 expect wget curl git build-essential \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& curl -sL https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get install -y oracle-java8-installer nodejs \  
&& apt-get autoclean \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install yarn  
  
# Install android SDK, tools and platforms  
RUN cd /opt && curl https://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz -o android-sdk.tgz && tar xzf android-sdk.tgz && rm
android-sdk.tgz  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
# accept license agreement  
RUN mkdir "$ANDROID_HOME/licenses" && echo -e
"\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license"  
  
RUN echo 'y' | /opt/android-sdk-linux/tools/android update sdk -u -a -t
platform-tools,build-tools-23.0.3,android-23,extra-android-support,extra-
google-m2repository,extra-android-m2repository  
  
# Install npm packages  
RUN npm i -g xcode-build-tools cordova ionic && npm cache clean  
  
# Create dummy app to build and preload gradle and maven dependencies  
RUN cd / && echo 'n' | ionic start app && cd /app && ionic platform add
android && ionic build android && rm -rf * .??* && rm
/root/.android/debug.keystore  
  
WORKDIR /app  

