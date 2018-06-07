FROM ubuntu:16.04  
MAINTAINER Martijn Brekhof "m.brekhof@gmail.com"  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
  
# ------------------------------------------------------  
# --- Install required tools  
RUN apt-get update -qq  
  
# Dependencies to execute Android builds  
RUN apt-get install -y openjdk-8-jdk wget expect unzip git lib32stdc++6  
  
WORKDIR /opt/  
RUN wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip  
  
ENV PATH
${PATH}:/opt/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools  
  
RUN mkdir ${ANDROID_HOME}  
WORKDIR ${ANDROID_HOME}  
RUN unzip /opt/sdk-tools-linux-3859397.zip  
RUN bash -c 'echo -e "y\ny\ny\ny\ny\ny\ny\n" | sdkmanager --licenses'  
RUN sdkmanager "platforms;android-26"  
RUN sdkmanager "platform-tools"  
RUN sdkmanager "build-tools;26.0.2"  
RUN sdkmanager "extras;google;m2repository"  
RUN sdkmanager "extras;android;m2repository"  
RUN sdkmanager "system-images;android-26;google_apis;x86"  
RUN sdkmanager "emulator"  
  
#Create an android emulator.  
#RUN avdmanager -v create avd -f -g google_apis -b x86 -d 'Nexus 5' -n test -c
100M -k 'system-images;android-26;google_apis;x86' -p
${ANDROID_HOME}/.android/  
#COPY config.ini ${ANDROID_HOME}/.android/avd/test.avd/  
RUN apt-get clean  

