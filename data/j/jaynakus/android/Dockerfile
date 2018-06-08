FROM ubuntu:14.04  
MAINTAINER Darren "dyhpoon@gmail.com"  
RUN apt-get update -qq  
  
# Dependencies to execute android  
RUN apt-get install -y --no-install-recommends openjdk-7-jdk lib32ncurses5
lib32stdc++6 lib32z1 wget git  
  
# Main Android SDK  
RUN cd /opt && wget -q http://dl.google.com/android/android-
sdk_r24.3.4-linux.tgz  
RUN cd /opt && tar xzf android-sdk_r24.3.4-linux.tgz  
RUN cd /opt && rm -f android-sdk_r24.3.4-linux.tgz  
  
# SET ENV  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Install All Build tools  
RUN android list sdk --all | grep -i "Android SDK Build-tools, revision
23.0.3" | cut -d '-' -f 1 | xargs -I {} sh -c 'echo y | android update sdk -u
-a -t {}'  
# Install Android API  
RUN echo y | android update sdk --filter android-23 --no-ui --force --all  
# Platform tools  
RUN android list sdk --all | grep -i "Android SDK Platform-tools" | cut -d '-'
-f 1 | xargs -I {} sh -c 'echo y | android update sdk -u -a -t {}'  
# Support libraries  
RUN echo y | android update sdk --filter extra-android-support --no-ui --force  
# Install Supprting Libraries  
RUN android list sdk --all | grep -i "\\(Google Repository\|Android Support
\\(Library\|Repository\\)\\)" | cut -d '-' -f 1 | xargs -I {} sh -c 'echo y |
android update sdk -u -a -t {}'  
  
# Cleaning  
RUN apt-get clean  

