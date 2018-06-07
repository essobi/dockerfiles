FROM openjdk:8  
  
MAINTAINER Alessandro Calzavara <alessandro.calzavara@voxnest.com>  
  
# Install Git and dependencies  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y file git curl zip libncurses5:i386 libstdc++6:i386
zlib1g:i386 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists /var/cache/apt  
  
# Set up environment variables  
ENV ANDROID_HOME="/home/user/android-sdk-linux" \  
SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip"
\  
GRADLE_URL="https://services.gradle.org/distributions/gradle-4.1-all.zip"  
# Create a non-root user  
RUN useradd -m user  
USER user  
WORKDIR /home/user  
  
# Install Gradle  
RUN wget $GRADLE_URL -O gradle.zip \  
&& unzip gradle.zip \  
&& mv gradle-4.1 gradle \  
&& rm gradle.zip \  
&& mkdir .gradle  
  
# Install Android SDK  
RUN mkdir "$ANDROID_HOME" .android \  
&& cd "$ANDROID_HOME" \  
&& curl -o sdk.zip $SDK_URL \  
&& unzip sdk.zip \  
&& rm sdk.zip  
  
# Install Android NDK  
#TODO  
# Download android platforms and tools  
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses  
RUN $ANDROID_HOME/tools/bin/sdkmanager "platforms;android-27" "build-
tools;27.0.2" "extras;google;google_play_services" "platform-tools"  
# Expose android paths to enviroment PATH  
ENV
PATH="/home/user/gradle/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:${PATH}"

