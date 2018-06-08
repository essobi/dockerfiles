############################################################  
# TCSJOHNHUXLEY GFL Build Image JDK7 #  
############################################################  
  
FROM ubuntu:16.04  
MAINTAINER Graham Stewart <graham.stewart@tcsjohnhuxley.com>  
USER root  
  
ENV LANG C.UTF-8  
  
RUN set -x && \  
export DEBIAN_FRONTEND=noninteractive && \  
echo "deb http://ppa.launchpad.net/openjdk-r/ppa/ubuntu xenial main" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 86F44E2A && \  
apt-get update && \  
apt-get install -y --no-install-recommends openjdk-7-jdk \  
git \  
openssh-client \  
binutils-avr \  
gcc-avr \  
avr-libc \  
srecord \  
maven \  
build-essential \  
bc \  
unzip \  
python \  
pkg-config \  
libcairo2-dev \  
curl && \  
apt-get install -y --no-install-recommends openjdk-8-jdk-headless && \  
curl -sL https://deb.nodesource.com/setup_0.12 | bash - && \  
mkdir -p /home/android/sdk && \  
cd /home/android/sdk && \  
curl -sL https://dl.google.com/android/repository/tools_r25.2.3-linux.zip -o
tools_r25.2.3-linux.zip && \  
unzip tools_r25.2.3-linux.zip && \  
rm tools_r25.2.3-linux.zip && \  
yes | /home/android/sdk/tools/bin/sdkmanager "build-tools;25.0.2" && \  
yes | /home/android/sdk/tools/bin/sdkmanager "platforms;android-17" && \  
apt-get install -y nodejs npm && \  
apt-get purge -y curl unzip openjdk-8-jdk-headless && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists && \  
mv /home/android/sdk/tools/source.properties /tmp && \  
rm -rf /home/android/sdk/tools && \  
mkdir /home/android/sdk/tools && \  
mv /tmp/source.properties /home/android/sdk/tools/ && \  
cd /usr/bin && \  
ln -s nodejs node  
  

