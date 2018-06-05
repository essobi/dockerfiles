# Build environment for Android Source  
FROM ubuntu:16.04  
MAINTAINER Mushroom <forever670@gmail.com>  
# skip interactive post-install configuration  
ENV DEBIAN_FRONTEND=noninteractive USER=build  
VOLUME /home/build/  
  
# Speed Download when in China  
# Install build dependencies (source:
http://source.android.com/source/initializing.html)  
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/' /etc/apt/sources.list &&
\  
apt-get -qq update && \  
apt-get -qqy upgrade && \  
apt-get install -y \  
git-core gnupg flex bison gperf build-essential zip curl zlib1g-dev gcc-
multilib g++-multilib libc6-dev-i386 lib32ncurses5-dev x11proto-core-dev
libx11-dev lib32z-dev ccache libgl1-mesa-dev libxml2-utils xsltproc unzip \  
openjdk-8-jdk python sudo  
  
# Add user # add sudo permission # Fix ownership  
RUN useradd build && \  
echo "build ALL=NOPASSWD: ALL" > /etc/sudoers.d/build && \  
chown -R build:build /home/build  
  
USER build  
WORKDIR /home/build  

