FROM java:8-jdk  
  
MAINTAINER Dmitry Rymarev  
  
ENV ANDROID_VERSION=24.4.1  
ENV ANDROID_API_LEVEL=23  
ENV ANDROID_BUILD_TOOLS_VERSION=23.0.3  
RUN curl -s -o android-sdk.tgz https://dl.google.com/android/android-
sdk_r$ANDROID_VERSION-linux.tgz  
RUN tar -xvzf android-sdk.tgz  
RUN rm -f android-sdk.tgz  
  
ENV ANDROID_HOME /android-sdk-linux  
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools  
  
RUN echo y | android update sdk --no-ui --all --filter platform-tools  
RUN echo y | android update sdk --no-ui --all --filter
android-$ANDROID_API_LEVEL  
RUN echo y | android update sdk --no-ui --all --filter build-
tools-$ANDROID_BUILD_TOOLS_VERSION  
RUN echo y | android update sdk --no-ui --all --filter extra-
android-m2repository  
RUN echo y | android update sdk --no-ui --all --filter extra-android-support  
  
RUN apt-get update && apt-get install -y \  
lib32stdc++6 \  
lib32z1  
  
ENV GRADLE_VERSION=2.13  
ENV GRADLE_HOME=/gradle-$GRADLE_VERSION  
  
RUN curl -s -o gradle-bin.zip
http://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip  
RUN unzip gradle-bin.zip -d /  
RUN rm -f gradle-bin.zip  
  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
ENV BUILD_DIR /build  
  
ONBUILD COPY . $BUILD_DIR  
  
ONBUILD WORKDIR $BUILD_DIR  

