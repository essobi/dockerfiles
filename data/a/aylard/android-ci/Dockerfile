# ===========================================  
# Android machine ready for CI from scratch  
# ===========================================  
FROM jedisct1/phusion-baseimage-latest  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
# ------------------------------------------------------  
# --- Dependencies to execute Android builds  
# ------------------------------------------------------  
RUN dpkg --add-architecture i386  
RUN apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget openjdk-8-jdk
libc6:i386 libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386  
  
# ------------------------------------------------------  
# --- Download Android SDK tools into $ANDROID_HOME  
# ------------------------------------------------------  
RUN cd /opt && wget --show-progress --progress="bar" -q
https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz -O android-sdk.tgz  
RUN cd /opt && tar -xvzf android-sdk.tgz  
RUN cd /opt && rm -f android-sdk.tgz  
  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# ------------------------------------------------------  
# --- Install Android SDKs and other build packages  
# ------------------------------------------------------  
# (!!!) Only install one package at a time, as "echo y" will only work for one
license!  
# If you don't do it this way you might get "Unknown response" in the logs,  
# but the android SDK tool **won't** fail, it'll just **NOT** install the
package.  
RUN echo y | android update sdk --no-ui --all --filter platform-tools | grep
'package installed'  
RUN echo y | android update sdk --no-ui --all --filter extra-android-support |
grep 'package installed'  
  
# SDKs  
# Please keep these in descending order!  
RUN echo y | android update sdk --no-ui --all --filter android-24 | grep
'package installed'  
  
# build tools  
# Please keep these in descending order!  
RUN echo y | android update sdk --no-ui --all --filter build-tools-24.0.0 |
grep 'package installed'  
  
# Android System Images, for emulators  
# Please keep these in descending order!  
RUN echo y | android update sdk --no-ui --all --filter sys-img-
armeabi-v7a-android-24 | grep 'package installed'  
  
# Extras  
RUN echo y | android update sdk --no-ui --all --filter extra-
android-m2repository | grep 'package installed'  
RUN echo y | android update sdk --no-ui --all --filter extra-
google-m2repository | grep 'package installed'  
RUN echo y | android update sdk --no-ui --all --filter extra-google-
google_play_services | grep 'package installed'  
  
# google apis  
# Please keep these in descending order!  
RUN echo y | android update sdk --no-ui --all --filter addon-google_apis-
google-24 | grep 'package installed'  
  
# ------------------------------------------------------  
# --- Install Gradle from PPA  
# ------------------------------------------------------  
RUN apt-get -y install gradle && gradle -v  
  
# if you want gradle gradle daemon enabled - not recommend for CI  
# RUN echo "org.gradle.daemon=true" >> ~/.gradle/gradle.properties  
# gradle heap - 10GB  
# RUN echo "org.gradle.jvmargs=-Xmx10752M" >> ~/.gradle/gradle.properties  
# ------------------------------------------------------  
# --- Install Maven 3 from PPA  
# ------------------------------------------------------  
RUN apt-get purge maven maven2  
RUN apt-get -y install maven && mvn --version  
  
# ------------------------------------------------------  
# --- Install required apps for compilation  
# ------------------------------------------------------  
RUN apt-get install -y git imagemagick rsync  
  
# ------------------------------------------------------  
# --- Cleanup and rev num  
# ------------------------------------------------------  
RUN apt-get clean  

