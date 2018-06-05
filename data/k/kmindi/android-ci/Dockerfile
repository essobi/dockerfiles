#  
# GitLab CI Android Runner  
#  
FROM openjdk:8-jdk  
LABEL maintainer="Kai Mindermann"  
  
# Up to date link for SDK TOOLS:
https://developer.android.com/studio/index.html#command-tools  
ENV VERSION_SDK_TOOLS="3859397" \  
ANDROID_BUILD_TOOLS="27.0.0" \  
ANDROID_HOME="/android-sdk"  
  
# emulator is in its own path since 25.3.0 (not in sdk tools anymore)  
ENV
PATH=$PATH:${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
# Prepare dependencies  
RUN mkdir $ANDROID_HOME \  
&& apt-get update \--yes \  
&& apt-get install --yes wget tar unzip lib32stdc++6 lib32z1 libqt5widgets5
expect net-tools \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install sdk tools  
RUN wget -O android-sdk.zip https://dl.google.com/android/repository/sdk-
tools-linux-${VERSION_SDK_TOOLS}.zip \  
&& unzip -q android-sdk.zip -d $ANDROID_HOME \  
&& rm android-sdk.zip  
  
# Workaround for  
# Warning: File /root/.android/repositories.cfg could not be loaded.  
# Workaround for host bitness error with android emulator  
# https://stackoverflow.com/a/37604675/455578  
RUN mkdir /root/.android && touch /root/.android/repositories.cfg \  
&& mv /bin/sh /bin/sh.backup && cp /bin/bash /bin/sh  
  
# Add adapted android-wait-for-emulator  
COPY android-wait-for-emulator.sh /usr/local/bin/android-wait-for-emulator  
RUN chmod +x /usr/local/bin/android-wait-for-emulator  
  
# Add own tools  
COPY assure_emulator_awake.sh /usr/local/bin/assure_emulator_awake.sh  
RUN chmod +x /usr/local/bin/assure_emulator_awake.sh  
  
# Update/Install platform and build tools, system images, extras, update
packages and list what packages (version) are installed  
RUN echo "y" | sdkmanager "tools" \  
&& echo "y" | sdkmanager "platform-tools" \  
&& echo "y" | sdkmanager "build-tools;${ANDROID_BUILD_TOOLS}" \  
&& echo "y" | sdkmanager "build-tools;26.0.2" \  
&& echo "y" | sdkmanager "platforms;android-27" \  
&& echo "y" | sdkmanager "platforms;android-26" \  
&& echo "y" | sdkmanager "platforms;android-25" \  
&& echo "y" | sdkmanager "system-images;android-27;google_apis;x86" \  
&& echo "y" | sdkmanager "system-images;android-26;google_apis;x86_64" \  
&& echo "y" | sdkmanager "system-images;android-26;google_apis;x86" \  
&& echo "y" | sdkmanager "system-images;android-25;google_apis;x86_64" \  
&& echo "y" | sdkmanager "system-images;android-25;google_apis;x86" \  
&& echo "y" | sdkmanager "extras;android;m2repository" \  
&& echo "y" | sdkmanager "extras;google;m2repository" \  
&& echo "y" | sdkmanager "extras;google;google_play_services" \  
&& echo "y" | sdkmanager
"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2" \  
&& echo "y" | sdkmanager
"extras;m2repository;com;android;support;constraint;constraint-layout-
solver;1.0.2" \  
&& echo "y" | sdkmanager --update \  
&& sdkmanager --list  

