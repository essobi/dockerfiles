#  
# Dockerfile for building ionic app  
#  
# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER Gavin Cho "gavin.cho@wubicu.com"  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Set locale  
RUN \  
locale-gen en_US.UTF-8 zh_TW.UTF-8  
  
ENV LANG zh_TW.UTF-8  
# Install prerequisites  
RUN \  
apt-get -y install software-properties-common; \  
add-apt-repository ppa:webupd8team/java; \  
apt-get update; \  
apt-get upgrade -y; \  
apt-get install -y build-essential lib32stdc++6 lib32z1 lib32bz2-1.0
lib32ncurses5 python; \  
echo "y" | apt-get -y install oracle-java7-installer; \  
apt-get -y install curl git vim; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Android SDK  
RUN \  
curl http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz | tar xz -C
/usr/local/; \  
chown root:root -R /usr/local/android-sdk-linux  
  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools  
  
# Install Node.js  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 5.5.0  
RUN \  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.30.2/install.sh |
bash && \  
source $NVM_DIR/nvm.sh && \  
nvm install v$NODE_VERSION && \  
nvm alias default v$NODE_VERSION && \  
nvm use default  
  
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
RUN \  
npm install -g gulp cordova ionic  
  
CMD node  

