# derived from https://hub.docker.com/r/mbertin/android_jdk-8/  
FROM bitriseio/docker-bitrise-base:latest  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
  
# ------------------------------------------------------  
# --- Install required tools  
RUN add-apt-repository ppa:openjdk-r/ppa -y  
RUN apt-get update -qq  
  
# Base (non android specific) tools  
# -> should be added to bitriseio/docker-bitrise-base  
# Dependencies to execute Android builds  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk
openjdk-7-jdk libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1  
  
# ------------------------------------------------------  
# --- Download Android SDK tools into $ANDROID_HOME  
RUN cd /opt && wget -q https://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz -O android-sdk.tgz  
RUN cd /opt && tar -xvzf android-sdk.tgz  
RUN cd /opt && rm -f android-sdk.tgz  
  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
# ------------------------------------------------------  
# --- Install Android SDKs and other build packages  
# Other tools and resources of Android SDK  
# you should only install the packages you need!  
# To get a full list of available options you can use:  
# android list sdk --no-ui --all --extended  
# (!!!) Only install one package at a time, as "echo y" will only work for one
license!  
# If you don't do it this way you might get "Unknown response" in the logs,  
# but the android SDK tool **won't** fail, it'll just **NOT** install the
package.  
RUN echo y | android update sdk --no-ui --all --filter platform-tools  
RUN echo y | android update sdk --no-ui --all --filter extra-android-support  
  
# google apis  
# Please keep these in descending order!  
RUN echo y | android update sdk --no-ui --all --filter addon-google_apis-
google-24  
RUN echo y | android update sdk --no-ui --all --filter addon-google_apis-
google-23  
  
# SDKs  
# Please keep these in descending order!  
RUN echo y | android update sdk --no-ui --all --filter android-24  
RUN echo y | android update sdk --no-ui --all --filter android-23  
  
# build tools  
# Please keep these in descending order!  
RUN echo y | android update sdk --no-ui --all --filter build-tools-24.0.1  
RUN echo y | android update sdk --no-ui --all --filter build-tools-24.0.0  
RUN echo y | android update sdk --no-ui --all --filter build-tools-23.0.3  
  
# Android System Images, for emulators  
# Please keep these in descending order!  
RUN echo y | android update sdk --no-ui --all --filter sys-img-
armeabi-v7a-android-24  
RUN echo y | android update sdk --no-ui --all --filter sys-img-
armeabi-v7a-android-23  
  
# Extras  
RUN echo y | android update sdk --no-ui --all --filter extra-
android-m2repository  
RUN echo y | android update sdk --no-ui --all --filter extra-
google-m2repository  
RUN echo y | android update sdk --no-ui --all --filter extra-google-
google_play_services  
  
# ------------------------------------------------------  
# --- Install Gradle from PPA  
# Gradle PPA  
RUN add-apt-repository ppa:cwchien/gradle  
RUN apt-get update  
RUN apt-get -y install gradle  
RUN gradle -v  
  
# ------------------------------------------------------  
# --- Cleanup and rev num  
# Cleaning  
RUN apt-get clean  
  
ENV BITRISE_DOCKER_REV_NUMBER_ANDROID 2016_01_09_1  
ENV JAVA8_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
ENV JAVA7_HOME /usr/lib/jvm/java-7-openjdk-amd64/  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
  
CMD bitrise -version  

