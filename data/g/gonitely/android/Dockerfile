FROM ubuntu:14.04.4  
MAINTAINER bitard [dot] michael [at] gmail [dot] com  
  
ENV DEBIAN_FRONTEND=noninteractive \  
ANDROID_HOME=/opt/android-sdk-linux \  
NODE_VERSION=5.6.0  
# Install basics  
RUN apt-get -qq update && \  
apt-get -qq install -y git wget curl unzip && \  
curl --retry 3 -SLO
"http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz"
&& \  
tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 && \  
rm "node-v$NODE_VERSION-linux-x64.tar.gz"  
  
#ANDROID  
#JAVA  
# install python-software-properties (so you can do add-apt-repository)  
RUN apt-get -qq update && apt-get -qq install -y -q python-software-properties
software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update && apt-get -y install oracle-java7-installer  
  
#ANDROID STUFF  
RUN echo ANDROID_HOME="${ANDROID_HOME}" >> /etc/environment && \  
dpkg --add-architecture i386 && \  
apt-get -qq update && \  
apt-get -qq install -y --force-yes expect ant wget libc6-i386 lib32stdc++6
lib32gcc1 lib32ncurses5 lib32z1 qemu-kvm kmod && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
  
# Install Android SDK  
cd /opt && \  
wget --output-document=android-sdk.tgz --quiet
http://dl.google.com/android/android-sdk_r23.0.1-linux.tgz && \  
tar xzf android-sdk.tgz && \  
rm -f android-sdk.tgz && \  
chown -R root. /opt  
  
# Setup environment  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:/opt/tools:${ANDROID_HOME}/build-tools/23.0.1  
# Install sdk elements  
COPY tools /opt/tools  
  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk -s --all
--no-ui --filter platform-tools"]  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk -s --all
--no-ui --filter tools"]  
RUN unzip -qq -o ${ANDROID_HOME}/temp/*.zip -d ${ANDROID_HOME}  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk -s --all
--no-ui --filter android-23"]  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk -s --all
--no-ui --filter build-tools-23.0.1"]  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk -s --all
--no-ui --filter extra-google-m2repository"]  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk -s --all
--no-ui --filter extra-android-m2repository"]  
  
RUN add-apt-repository ppa:brightbox/ruby-ng -y && \  
apt-get -qq update > /dev/null && \  
apt-get -qq install -y build-essential ruby2.0-dev ruby2.0 > /dev/null && \  
gem install -q fastlane supply sass > /dev/null  
  
RUN npm install -g --silent grunt-cli@0.1.13 \  
bower@1.7.7 \  
cordova@6.2.0 \  
cordova-common@1.4.1 \  
ionic@2.0.0 && \  
npm cache clear  
  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk -s --all
--no-ui --filter extra"]  

