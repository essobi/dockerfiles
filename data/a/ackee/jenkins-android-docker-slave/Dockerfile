FROM jenkinsci/jnlp-slave  
#FROM bitriseio/docker-bitrise-base-alpha:latest  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
# ------------------------------------------------------  
# --- Install required tools  
USER root  
  
# Dependencies to execute Android builds  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk libc6:i386
libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386 || apt-get install -f
&& \  
rm -rf /var/lib/apt/lists/*  
  
# ------------------------------------------------------  
# --- Download Android SDK tools into $ANDROID_HOME  
RUN cd /opt && wget -q https://dl.google.com/android/repository/sdk-tools-
linux-4333796.zip -O android-sdk-tools.zip && \  
unzip -q android-sdk-tools.zip && mkdir -p ${ANDROID_HOME} && mv tools/
${ANDROID_HOME}/tools/ && \  
rm -f android-sdk-tools.zip  
  
# ndk-bundle  
RUN cd /opt/android-sdk-linux/ && wget -q
https://dl.google.com/android/repository/android-ndk-r15c-linux-x86_64.zip -O
ndk-bundle.zip && \  
unzip -q ndk-bundle.zip && mv android-ndk-r15c ndk-bundle && chown -R
jenkins:jenkins ndk-bundle/  
  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
  
# Accept licenses before installing components, no need to echo y for each
component  
# License is valid for all the standard components in versions installed from
this file  
# Non-standard components: MIPS system images, preview versions, GDK (Google
Glass) and Android Google TV require separate licenses, not accepted there  
RUN yes | sdkmanager --licenses  
  
# Platform tools  
RUN sdkmanager "platform-tools"  
  
# Emulator  
# RUN sdkmanager "emulator"  
# For now we'll keep using 26.1.2 ; 26.1.3 had some booting issues...  
RUN cd /opt \  
&& wget https://dl.google.com/android/repository/emulator-linux-4077558.zip -O
emulator.zip \  
&& unzip -q emulator.zip -d ${ANDROID_HOME} \  
&& rm emulator.zip  
  
# Please keep all sections in descending order!  
RUN yes | sdkmanager \  
"platforms;android-27" \  
"platforms;android-26" \  
"platforms;android-25" \  
"platforms;android-24" \  
"platforms;android-23" \  
"platforms;android-22" \  
"platforms;android-21" \  
"build-tools;27.0.1" \  
"build-tools;27.0.0" \  
"build-tools;26.0.2" \  
"build-tools;26.0.1" \  
"build-tools;25.0.3" \  
"build-tools;24.0.3" \  
"build-tools;23.0.3" \  
"build-tools;22.0.1" \  
"build-tools;21.1.2" \  
"build-tools;19.1.0" \  
"build-tools;17.0.0" \  
"system-images;android-25;google_apis;armeabi-v7a" \  
"system-images;android-24;default;armeabi-v7a" \  
"system-images;android-22;default;armeabi-v7a" \  
"system-images;android-21;default;armeabi-v7a" \  
"system-images;android-19;default;armeabi-v7a" \  
"extras;android;m2repository" \  
"extras;google;m2repository" \  
"extras;google;google_play_services" \  
"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2" \  
"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.1" \  
"add-ons;addon-google_apis-google-23" \  
"add-ons;addon-google_apis-google-22" \  
"add-ons;addon-google_apis-google-21"  
# ------------------------------------------------------  
# --- Install Gradle from PPA  
# Gradle PPA  
RUN apt-get update && \  
apt-get -y install gradle && \  
gradle -v && \  
rm -rf /var/lib/apt/lists/*  
  
# ------------------------------------------------------  
# --- Install Maven 3 from PPA  
  
RUN apt-get -y purge maven && \  
apt-get update && \  
apt-get -y install maven && \  
mvn --version && \  
rm -rf /var/lib/apt/lists/*  
  
# ------------------------------------------------------  
# --- Install Fastlane  
#RUN gem install fastlane --no-document  
#RUN fastlane --version  
# fix HOME root env variables for android emulator plugin...  
#WORKDIR /root  
#ENV HOME /root  
#RUN usermod -d /root jenkins && chown -R jenkins:root /root && \  
# chown -R jenkins:jenkins $ANDROID_HOME && chmod -R g+w $ANDROID_HOME  
  
CMD bitrise -version  

