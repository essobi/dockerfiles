FROM openjdk:8-jdk  
MAINTAINER Florian Baader <florian.baader@selectcode.de>  
  
ENV ANDROID_TARGET_SDK="27" \  
ANDROID_BUILD_TOOLS="26.0.2"  
RUN apt-get --quiet update --yes  
RUN apt-get --quiet install --yes wget tar unzip lib32stdc++6 lib32z1  
  
RUN wget --quiet --output-document=android-sdk.zip
https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \  
unzip android-sdk.zip -d android-sdk-linux/  
  
RUN echo y | android-sdk-linux/tools/bin/sdkmanager
"platforms;android-${ANDROID_TARGET_SDK}"  
RUN echo y | android-sdk-linux/tools/bin/sdkmanager "tools"  
RUN echo y | android-sdk-linux/tools/bin/sdkmanager "build-
tools;${ANDROID_BUILD_TOOLS}"  
  
RUN echo y | android-sdk-linux/tools/bin/sdkmanager
"extras;android;m2repository"  
RUN echo y | android-sdk-linux/tools/bin/sdkmanager
"extras;google;google_play_services"  
RUN echo y | android-sdk-linux/tools/bin/sdkmanager
"extras;google;m2repository"  
  
ENV ANDROID_HOME $PWD/android-sdk-linux  
  

