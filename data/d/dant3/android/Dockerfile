FROM java:openjdk-8-jdk  
  
MAINTAINER Viacheslav Blinov "blinov.vyacheslav@gmail.com"  
  
# Installs i386 architecture required for running 32 bit Android tools  
# rm -rf /var/lib/apt/lists/* && \  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 expect
&& \  
apt-get autoremove -y && \  
apt-get clean  
  
  
# Install android sdk related tools  
COPY tools /opt/tools  
ENV PATH ${PATH}:/opt/tools  
  
ENV ANDROID_SDK_VERSION r24.4.1  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
# Install Android SDK  
# chown -R root.root android-sdk-linux && \  
RUN cd /opt && \  
wget --output-document=android-sdk.tgz --quiet
http://dl.google.com/android/android-sdk_${ANDROID_SDK_VERSION}-linux.tgz && \  
tar xzf android-sdk.tgz && \  
rm -f android-sdk.tgz && \  
android-accept-licenses.sh $ANDROID_HOME/tools/android update sdk --all \--no-
ui --filter tools && \  
android-accept-licenses.sh $ANDROID_HOME/tools/android update sdk --all \--no-
ui --filter tools  
  
# Setup environment  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Check installation  
RUN which android  
  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter platform-tools  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter extra-android-support  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter extra-android-m2repository  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter extra-google-m2repository  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter extra-google-google_play_services  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter android-23  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter android-22  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter build-tools-25.0.2  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter build-tools-25.0.3  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter build-tools-23.0.3  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter build-tools-23.0.1  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter build-tools-22.0.1  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter sys-img-x86-android-23  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter ndk-bundle  
RUN /opt/tools/android-accept-licenses.sh android update sdk --all \--no-ui
--filter sys-img-armeabi-v7a-android-23  
  
# create emulator to run tests:  
# RUN echo "no" | android create avd \  
# --force \  
# --device "Nexus 5" \  
# --name test \  
# --target android-23 \  
# --abi x86 \  
# --skin WVGA800 \  
# --sdcard 512M  
  
# start this emulator:  
# RUN emulator -avd test && /opt/tools/android-wait-emulator.sh  
  
# Check android sdk packages installation  
RUN which adb  
  
# GO to workspace  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace  

