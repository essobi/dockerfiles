FROM openjdk:8-jdk  
  
RUN apt-get \--quiet update \--yes && \  
apt-get \--quiet install \--yes wget tar unzip lib32stdc++6 lib32z1 gradle
yarn apt-transport-https && \  
apt remove \--yes cmdtest && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get \--quiet install \--yes yarn && \  
apt-get clean  
  
ENV ANDROID_COMPILE_SDK="27" ANDROID_BUILD_TOOLS="27.0.0"
ANDROID_SDK_TOOLS="3859397" ANDROID_HOME="/opt" NODE_VER="6.11.3"
PATH="/opt/node/bin:/opt/tools:/opt/tools/bin:${PATH}"  
  
RUN cd /opt && \  
wget \--quiet \--output-document=android-sdk.zip
https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_TOOLS}.zip && \  
unzip android-sdk.zip && rm android-sdk.zip && ls tools && \  
wget \--quiet \--output-document=node.tar.xz
https://nodejs.org/dist/v${NODE_VER}/node-v${NODE_VER}-linux-x64.tar.xz && \  
tar -xf node.tar.xz && rm node.tar.xz && \  
mv /opt/node-v${NODE_VER}-linux-x64 /opt/node && \  
yes | sdkmanager \--licenses && \  
npm install -g phonegap cordova ionic  
  
RUN touch ~/.android/repositories.cfg && sdkmanager "platform-tools"
"platforms;android-${ANDROID_COMPILE_SDK}"
"extras;google;google_play_services" "extras;google;m2repository"
"extras;android;m2repository" "tools" "ndk-bundle" "build-
tools;$ANDROID_BUILD_TOOLS"  
  
RUN echo yes | sdkmanager \--licenses  

