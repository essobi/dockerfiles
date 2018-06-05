FROM ubuntu:16.04  
MAINTAINER Aurelian Dumanovschi <aurasd@gmail.com>  
  
ENV AGENT_DIR /opt/workspace  
ENV GRADLE_USER_HOME /opt/gradle  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV ANDROID_NDK_HOME /opt/android-sdk-linux/ndk-bundle  
ENV NDK_HOME /opt/android-sdk-linux/ndk-bundle  
ENV ANDROID_SDK_TOOLS_VERSION 3859397  
ENV EMULATOR_PLATFORM android-27  
ENV EMULATOR_VARIANT google_apis_playstore  
ENV EMULATOR_ABI x86  
ENV EMULATOR_PACKAGE "system-
images;$EMULATOR_PLATFORM;$EMULATOR_VARIANT;$EMULATOR_ABI"  
ENV EMULATOR_VARIANT_ABI "$EMULATOR_VARIANT/$EMULATOR_ABI"  
ENV SHELL /bin/bash  
ENV PATH "$ANDROID_HOME/emulator:$PATH"  
ENV PATH "$ANDROID_HOME/platform-tools:$PATH"  
ENV PATH "$ANDROID_HOME/tools/bin:$PATH"  
ENV PATH "$ANDROID_HOME/tools:$PATH"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends software-properties-common
python-software-properties \  
&& apt-add-repository ppa:brightbox/ruby-ng \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
aufs-tools wget file language-pack-en sudo openjdk-8-jdk default-jdk libpulse0
libx11-6 \  
libgl1-mesa-glx mesa-utils pciutils ruby2.4 ruby2.4-dev ruby ruby-switch unzip
lxc \  
fontconfig libffi-dev build-essential git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Fix locale.  
ENV LANG en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
RUN locale-gen en_US && update-locale LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8  
  
# Install fastlane  
RUN ruby-switch --set ruby2.4  
RUN gem install fastlane -NV --no-rdoc --no-ri  
  
RUN mkdir -p $GRADLE_USER_HOME  
RUN mkdir -p $ANDROID_HOME  
  
# Install Android command line tools  
RUN wget -nc https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_TOOLS_VERSION}.zip \  
&& unzip sdk-tools-linux-${ANDROID_SDK_TOOLS_VERSION}.zip -d $ANDROID_HOME \  
&& rm sdk-tools-linux-${ANDROID_SDK_TOOLS_VERSION}.zip \  
&& chmod +x $ANDROID_HOME/tools/android  
  
# Install Android licenses to not accept them manually during builds  
ADD licenses.tar.gz $ANDROID_HOME/  
  
# Prepare for the emulator  
RUN mkdir $ANDROID_HOME/system-images \  
&& mkdir $HOME/.android \  
&& mkdir $HOME/.android/avd \  
&& ln -s $ANDROID_HOME/system-images $HOME/.android/avd/system-images  
  
# Install packages  
RUN $ANDROID_HOME/tools/bin/sdkmanager "extras;google;m2repository" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "extras;google;google_play_services" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "cmake;3.6.4111459" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "lldb;2.3" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "ndk-bundle" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "patcher;v4" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "emulator" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "platforms;$EMULATOR_PLATFORM" \  
&& $ANDROID_HOME/tools/bin/sdkmanager "$EMULATOR_PACKAGE"  
  
VOLUME /opt/android-sdk-linux  
VOLUME /opt/gradle  
  
EXPOSE 9090

