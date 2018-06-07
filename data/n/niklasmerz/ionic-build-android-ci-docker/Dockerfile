FROM ubuntu:16.04  
MAINTAINER Niklas Merz  
  
# Install apt packages  
RUN apt-get update && apt-get install --yes curl unzip wget  
RUN curl --silent --location https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y git lib32stdc++6 lib32z1 nodejs s3cmd build-essential
openjdk-8-jdk-headless sendemail libio-socket-ssl-perl libnet-ssleay-perl &&
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Install android SDK, tools and platforms  
RUN cd /opt && curl https://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz -o android-sdk.tgz && tar xzf android-sdk.tgz && rm
android-sdk.tgz  
ENV ANDROID_HOME /opt/android-sdk-linux  
RUN echo 'y' | /opt/android-sdk-linux/tools/android update sdk --no-ui -a -t
platform-tools,build-tools-23.0.3,android-23,extra-android-support,extra-
google-m2repository,extra-android-m2repository  
RUN mkdir "$ANDROID_HOME/licenses" && echo -e
"\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license"  
# Install npm packages  
RUN npm i -g cordova ionic gulp bower grunt phonegap && npm cache clean  
  
# Create dummy app to build and preload gradle and maven dependencies  
RUN git config --global user.email "you@example.com" && git config --global
user.name "Your Name"  
RUN wget https://services.gradle.org/distributions/gradle-4.1-bin.zip && mkdir
/opt/gradle && unzip -d /opt/gradle gradle-4.1-bin.zip  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin::/opt/gradle/gradle-4.1/bin  
RUn gradle -v  
RUN cd / && echo 'n' | ionic start --no-interactive --no-link app blank && cd
/app && ionic --no-interactive cordova platform add android && cordova build
android && rm -rf * .??*  
  
WORKDIR /app  

