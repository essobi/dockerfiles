# Some stuff from
https://0xacab.org/leap/bitmask_android/blob/a7b4f463e4ffc282814ef74daf18c74581fc3a7d/docker/android-
sdk.dockerfile  
FROM arris/dev:latest  
  
ENV ANDROID_HOME /opt/android/sdk  
ENV SDK_TOOLS_VERSION "25.2.5"  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
# ENV ANDROID_NDK_HOME ${ANDROID_HOME}/ndk-bundle  
# ENV PATH ${PATH}:${ANDROID_NDK_HOME}  
  
# Node  
# Watchman Deps  
# Android SDK Deps  
ARG APT_PACKAGES='nodejs nodejs-legacy yarn \  
autoconf automake build-essential python-dev libssl-dev libtool pkg-config \  
unzip openjdk-8-jdk maven make clang lib32stdc++6 lib32z1'  
ARG YARN_PACKAGES='react-native-cli react-native-git-upgrade'  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN \  
# Apt Sources  
apt-get update -y \  
# Node - See: https://nodejs.org/en/download/package-manager/#debian-and-
ubuntu-based-linux-distributions  
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - \  
# Yarn - https://yarnpkg.com/lang/en/docs/install/#linux-tab  
&& apt-get install -yq gnupg \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list \  
# Apt Packages  
&& apt-get update -y \  
&& apt-get install -yq ${APT_PACKAGES} \  
# Yarn Packages  
&& export PATH="`yarn global bin`:${PATH}" \  
&& yarn global add ${YARN_PACKAGES} \  
# Watchman  
&& cd /tmp \  
&& git clone https://github.com/facebook/watchman.git \  
&& cd watchman/ \  
&& git checkout v4.9.0 \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
# Android SDK  
&& cd /opt \  
&& mkdir -p ${ANDROID_HOME} \  
&& wget -q -O sdk-tools.zip
https://dl.google.com/android/repository/tools_r${SDK_TOOLS_VERSION}-linux.zip
\  
&& unzip -q sdk-tools.zip -d ${ANDROID_HOME} \  
&& rm -f sdk-tools.zip \  
# HACK :(  
&& mkdir -p ~/.android && touch ~/.android/repositories.cfg \  
# Install Platform Tools Package  
&& echo y | sdkmanager "platform-tools" \  
# Install Android Support Repositories  
&& echo y | sdkmanager "extras;android;m2repository" \  
# Install Target SDK Packages (Please keep in descending order)  
&& echo y | sdkmanager "platforms;android-25" \  
&& echo y | sdkmanager "platforms;android-24" \  
&& echo y | sdkmanager "platforms;android-23" \  
# Install Build Tools (Please keep in descending order)  
&& echo y | sdkmanager "build-tools;25.0.2" \  
&& echo y | sdkmanager "build-tools;24.0.3" \  
&& echo y | sdkmanager "build-tools;23.0.3" \  
# Install NDK packages from sdk tools  
# && echo y | sdkmanager "ndk-bundle"  
# && echo y | sdkmanager "cmake;3.6.3155560"  
# && echo y | sdkmanager "lldb;2.3"  
# --- Install Android Emulator  
# && echo y | sdkmanager "emulator"  
# System Images for emulators  
# && echo y | sdkmanager "system-images;android-25;google_apis;armeabi-v7a"  
# && echo y | sdkmanager "system-images;android-24;google_apis;armeabi-v7a"  
# && echo y | sdkmanager "system-images;android-23;google_apis;armeabi-v7a"  
# && echo y | sdkmanager "system-images;android-23;google_apis;arm64-v8a"  
&& apt-get clean  
  
EXPOSE 5037 8081 19000 19001  
COPY config/android /root/.android  
COPY config/supervisor/react.conf /etc/supervisor/conf.d/react.conf  
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/react.conf  

