FROM ubuntu:14.04  
MAINTAINER White World "ljq258@gmail.com"  
# Install prerequisites.  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get -y install lib32z1 lib32ncurses5 lib32bz2-1.0 lib32stdc++6  
RUN echo "y" | apt-get -y install oracle-java7-installer  
RUN apt-get -y install zip unzip curl  
  
# Install Android development environment.  
RUN curl -L -O http://dl.google.com/android/android-sdk_r24.3.3-linux.tgz &&
tar xf android-sdk_r24.3.3-linux.tgz  
RUN curl -L -O https://services.gradle.org/distributions/gradle-2.5-bin.zip &&
unzip gradle-2.5-bin.zip  
  
# Set environment variables.  
ENV GRADLE_HOME /gradle-2.5  
ENV ANDROID_HOME /android-sdk-linux  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Update the SDK with some tooling.  
RUN echo "y" | android update sdk -u -a --filter platform-
tools,android-21,build-tools-22.0.0,extra-google-m2repository,extra-
android-m2repository,extra-android-support  
  
# Set /android as code directory  
WORKDIR /android  
# RUN git clone ...  
# Gradle  
# RUN gradle assembleDebug

