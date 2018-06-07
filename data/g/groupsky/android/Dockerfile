FROM ubuntu:trusty  
  
ARG ANDROID_SDK_VERSION  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Deps  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get update && \  
apt-get install -y software-properties-common && \  
dpkg --add-architecture i386 && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y --force-yes \  
ant \  
maven \  
gradle \  
oracle-java8-installer \  
expect \  
git \  
wget \  
libc6-i386 \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
python \  
curl && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
ENV ANDROID_SDK_VERSION=${ANDROID_SDK_VERSION:-r24.4.1}  
  
# Install Android SDK  
RUN cd /opt && \  
wget -O android-sdk.tgz -q http://dl.google.com/android/android-
sdk_${ANDROID_SDK_VERSION}-linux.tgz && \  
tar xzf android-sdk.tgz && \  
rm -f android-sdk.tgz && \  
chown -R root.root android-sdk-linux  
  
# Setup environment  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle \  
ANDROID_HOME=/opt/android-sdk-linux \  
PATH=${PATH}:/opt/android-sdk-linux/tools:/opt/android-sdk-linux/platform-
tools  
  
# Install sdk elements  
COPY tools /opt/tools  
ENV PATH ${PATH}:/opt/tools  
RUN android-accept-licenses.sh \  
"android update sdk --all --force --no-ui --filter add-on,platform,platform-
tool,tool,`android list sdk --no-ui -e -a | grep build-tools | cut '-d"' -f2 |
tr '\n' ','`"  

