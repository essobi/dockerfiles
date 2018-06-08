FROM openjdk:8-jdk  
LABEL maintainer="jst@linux.com"  
  
ENV ANDROID_HOME="/sdk" \  
VERSION_BUILD_TOOLS="26.0.2" \  
VERSION_SDK="3952940" \  
VERSION_TARGET_SDK="26"  
ENV
PATH=${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools:${PATH}  
  
RUN wget -nv https://dl.google.com/android/repository/sdk-tools-
linux-${VERSION_SDK}.zip -O /sdk-tools.zip &&\  
unzip -q /sdk-tools.zip -d ${ANDROID_HOME} &&\  
rm /sdk-tools.zip  
  
RUN mkdir ~/.android && touch ~/.android/repositories.cfg  
  
RUN yes | sdkmanager --licenses && sdkmanager --update  
  
RUN sdkmanager \  
"build-tools;${VERSION_BUILD_TOOLS}" \  
"extras;android;m2repository" \  
"extras;google;google_play_services" \  
"extras;google;m2repository" \  
"platform-tools" \  
"platforms;android-${VERSION_TARGET_SDK}" \  
"tools"  

