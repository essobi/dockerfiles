# Android Dockerfile  
  
FROM openjdk:8-jdk  
  
MAINTAINER Duy "duy@dwork.vn"  
  
# Sets language to UTF8 : this works in pretty much all cases  
ENV LANG en_US.UTF-8  
  
ENV DOCKER_ANDROID_LANG en_US  
ENV DOCKER_ANDROID_DISPLAY_NAME mobileci-docker  
  
ENV ANDROID_COMPILE_SDK "25"  
ENV ANDROID_BUILD_TOOLS "24.0.0"  
ENV ANDROID_SDK_TOOLS "24.4.1"  
  
  
# Never ask for confirmations  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get \--quiet update \--yes  
RUN apt-get \--quiet install --yes wget tar unzip lib32stdc++6 lib32z1  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get clean  
  
RUN wget --quiet --output-document=android-sdk.tgz
https://dl.google.com/android/android-sdk_r$ANDROID_SDK_TOOLS-linux.tgz  
RUN tar --extract --gzip --file=android-sdk.tgz  
RUN rm android-sdk.tgz  
  
  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter android-${ANDROID_COMPILE_SDK}  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter platform-tools  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter build-tools-${ANDROID_BUILD_TOOLS}  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter extra-android-m2repository  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter extra-google-google_play_services  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
\--filter extra-google-m2repository  
  
ENV ANDROID_HOME "$PWD/android-sdk-linux"  
ENV PATH "$PATH:$PWD/android-sdk-linux/platform-tools/""  
  
RUN mkdir -p "$ANDROID_HOME/licenses" || true  
RUN echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license"  
RUN echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"$ANDROID_HOME/licenses/android-sdk-preview-license"  

