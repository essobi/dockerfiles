############################################################  
# Dockerfile to build Okapi Installed Containers  
# Based on Ubuntu:latest  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
  
# File Author / Maintainer  
MAINTAINER Maintaner Tom Wu <tomoodesign@gmail.com>  
  
# Pre-requisite for compiling Okapi  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y \  
gcc \  
gcc-multilib \  
libc6-i386 \  
make \  
bison \  
flex \  
openjdk-6-jdk:i386 \  
git \  
vim && \  
rm -rf /var/lib/apt/lists/* && \  
cp /usr/lib/jvm/java-1.6.0-openjdk-i386/include/jni.h
/usr/lib/gcc/x86_64-linux-gnu/4.8/include && \  
cp /usr/lib/jvm/java-1.6.0-openjdk-i386/include/jni_md.h
/usr/lib/gcc/x86_64-linux-gnu/4.8/include && \  
mkdir -p /home/okapi  
  
ADD okapi/* /home/okapi/  
  
# initialize okapi  
ENTRYPOINT ["/home/okapi/scripts/init.sh"]  
  
WORKDIR /home/okapi  
  

