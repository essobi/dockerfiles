FROM openjdk:8-jdk  
  
# 作成者情報  
MAINTAINER toshi <toshi@toshi.click>  
  
# set Env  
ENV ANDROID_SDK_TOOLS "3859397"  
ENV ANDROID_BUILD_TOOLS "27.0.3"  
ENV ANDROID_COMPILE_SDK "27"  
ENV SDK_ROOT "/sdk"  
RUN apt-get --quiet update --yes  
RUN apt-get --quiet install --yes wget tar unzip lib32stdc++6 lib32z1  
RUN wget --quiet --output-document=android-sdk.zip
https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_TOOLS}.zip  
RUN unzip -qq android-sdk.zip -d ${SDK_ROOT}  
RUN mkdir -p /root/.android  
RUN touch /root/.android/repositories.cfg  
RUN mkdir -p ${SDK_ROOT}/licenses  
RUN echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
${SDK_ROOT}/licenses/android-sdk-license  
RUN echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
${SDK_ROOT}/licenses/android-sdk-preview-license  
RUN echo y | ${SDK_ROOT}/tools/bin/sdkmanager "tools" >/dev/null 2>&1  
RUN echo y | ${SDK_ROOT}/tools/bin/sdkmanager
"platforms;android-${ANDROID_COMPILE_SDK}" >/dev/null 2>&1  
RUN echo y | ${SDK_ROOT}/tools/bin/sdkmanager "build-
tools;${ANDROID_BUILD_TOOLS}" >/dev/null 2>&1  
RUN echo y | ${SDK_ROOT}/tools/bin/sdkmanager "extras;android;m2repository"
>/dev/null 2>&1  
RUN echo y | ${SDK_ROOT}/tools/bin/sdkmanager
"extras;google;google_play_services" >/dev/null 2>&1  
RUN echo y | ${SDK_ROOT}/tools/bin/sdkmanager "extras;google;m2repository"
>/dev/null 2>&1  
ENV ANDROID_HOME ${SDK_ROOT}  
ENV ANDROID_NDK_HOME ${SDK_ROOT}/ndk-bundle/  
ENV PATH $PATH:${SDK_ROOT}/platform-tools/  
RUN touch local.properties  
RUN echo "sdk.dir=${ANDROID_HOME}" >> local.properties  
RUN echo "ndk.dir=${ANDROID_NDK_HOME}" >> local.properties  

