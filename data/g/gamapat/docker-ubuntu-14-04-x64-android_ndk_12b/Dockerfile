# This docker file contains build environment  
FROM ubuntu:14.04  
MAINTAINER kleymenov.nikita <kleymenov.nikita@apriorit.com>  
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl wget git
unzip tar make cmake gcovr && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean  
RUN mkdir /tmp/build && cd /tmp/build && wget
https://dl.google.com/android/repository/android-ndk-r12b-linux-x86_64.zip &&
\  
unzip android-ndk-r12b-linux-x86_64.zip

