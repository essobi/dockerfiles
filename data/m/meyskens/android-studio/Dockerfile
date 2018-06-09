FROM openjdk:8-jdk  
  
## This image is based on  
## https://github.com/circleci/circleci-images  
## many thanks for this!  
ARG sdk_version=sdk-tools-linux-3859397.zip  
ARG android_home=/opt/android/sdk  
ARG studio_url=https://dl.google.com/dl/android/studio/ide-
zips/3.0.1.0/android-studio-ide-171.4443003-linux.zip  
  
RUN apt-get update && \  
apt-get install --yes xvfb gcc-multilib lib32z1 lib32stdc++6 build-essential  
  
# Download and install Android SDK  
RUN mkdir -p ${android_home} && \  
curl --silent --show-error --location --fail --retry 3 --output
/tmp/${sdk_version} https://dl.google.com/android/repository/${sdk_version} &&
\  
unzip -q /tmp/${sdk_version} -d ${android_home} && \  
rm /tmp/${sdk_version}  
  
# Set environmental variables  
ENV ANDROID_HOME ${android_home}  
ENV ADB_INSTALL_TIMEOUT 120  
ENV
PATH=${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools:${PATH}  
  
RUN mkdir ~/.android && echo '### User Sources for Android SDK Manager' >
~/.android/repositories.cfg  
  
RUN sdkmanager --update && yes | sdkmanager --licenses  
  
# Update SDK manager and install system image, platform and build tools  
RUN sdkmanager \  
"tools" \  
"platform-tools" \  
"emulator" \  
"extras;android;m2repository" \  
"extras;google;m2repository" \  
"extras;google;google_play_services"  
  
RUN sdkmanager \  
"build-tools;25.0.0" \  
"build-tools;25.0.1" \  
"build-tools;25.0.2" \  
"build-tools;25.0.3" \  
"build-tools;26.0.1" \  
"build-tools;26.0.2"  
  
RUN sdkmanager "platforms;android-25"  
RUN sdkmanager "platforms;android-26"  
  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout;1.0.2"  
  
## So that was the SDK folks  
## Preadd an emulator  
# Add deps  
RUN apt-get install -y file mesa-utils  
  
RUN sdkmanager "system-images;android-25;google_apis;x86_64"  
  
RUN echo no | avdmanager \  
create avd --name emulator \  
\--package 'system-images;android-25;google_apis;x86_64'  
  
## Now the studio  
RUN apt-get install -y wget  
  
RUN wget -O studio.zip ${studio_url} &&\  
unzip -d /opt/ studio.zip &&\  
rm -f studio.zip  
  
## gradle  
RUN wget https://services.gradle.org/distributions/gradle-4.1-bin.zip &&\  
mkdir /opt/gradle p &&\  
unzip -d /opt/gradle gradle-4.1-bin.zip &&\  
rm -f gradle-4.1-bin.zip  
  
ENV PATH=$PATH:/opt/gradle/gradle-4.1/bin  
  
  
CMD /opt/android-studio/bin/studio.sh  

