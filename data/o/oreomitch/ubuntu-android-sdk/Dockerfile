#######################################################################  
# Dockerfile to build an Ubuntu Android SDK container image  
# Based on Ubuntu  
#######################################################################  
  
# Set the base image to Ubuntu  
FROM oreomitch/ubuntu-jdk:14.04-JDK7  
# File Author / Maintainer  
MAINTAINER Mitchell Wong Ho <oreomitch@gmail.com>  
  
# Add Android SDK  
RUN apt-get update  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install wget tmux build-essential software-properties-common
python-software-properties -y  
  
RUN wget --progress=dot:giga http://dl.google.com/android/android-
sdk_r23.0.2-linux.tgz  
RUN mkdir /opt/android  
RUN tar -C /opt/android -xzvf ./android-sdk_r23.0.2-linux.tgz  
ENV ANDROID_HOME /opt/android/android-sdk-linux  
ENV PATH $ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH  
RUN chmod -R 744 $ANDROID_HOME  
  
VOLUME ["/opt/android/android-sdk-linux"]  

