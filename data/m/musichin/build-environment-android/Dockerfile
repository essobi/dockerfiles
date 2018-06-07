FROM ubuntu:16.04  
MAINTAINER Anton Musichin  
  
# Update apt-get  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
  
# Install packages  
RUN apt-get install -y \  
locales \  
autoconf \  
software-properties-common \  
build-essential \  
curl \  
wget \  
git \  
unzip \  
openjdk-8-jdk \  
\--no-install-recommends  
  
# Set language to UTF8  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
  
# Clean up apt-get  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get clean  
  
# Install Android SDK  
RUN wget -q https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip -O sdk-tools-linux.zip  
RUN unzip -q sdk-tools-linux.zip -d /usr/local/android-sdk  
RUN rm sdk-tools-linux.zip  
RUN echo y | /usr/local/android-sdk/tools/bin/sdkmanager \  
"tools" \  
"platform-tools" \  
"extras;google;m2repository" \  
"extras;android;m2repository" \  
"platforms;android-27" \  
"build-tools;27.0.3"  
ENV ANDROID_HOME /usr/local/android-sdk  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
ENV PATH $PATH:$ANDROID_HOME/build-tools/27.0.3  
RUN chmod -R a+rx $ANDROID_HOME  
  
# Prepare project directory  
ENV PROJECT /project  
RUN mkdir $PROJECT  
WORKDIR $PROJECT  
RUN echo "sdk.dir=$ANDROID_HOME" > local.properties  

