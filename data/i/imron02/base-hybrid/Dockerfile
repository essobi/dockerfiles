FROM node:8.11.2  
# Install basic  
RUN apt-get update \  
&& apt-get install -y unzip \  
&& apt-get install -y --no-install-recommends apt-utils  
  
# Install Java  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle/  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get -y install oracle-java8-installer  
  
# Install Android SDK  
ENV ANDROID_HOME=/opt/android-sdk-linux  
  
RUN mkdir "${ANDROID_HOME}" \  
&& echo ANDROID_HOME="${ANDROID_HOME}" >> /etc/environment \  
&& wget --quiet https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip \  
&& unzip sdk-tools-linux-3859397.zip -d "${ANDROID_HOME}" \  
&& rm sdk-tools-linux-3859397.zip  
  
RUN yes | "${ANDROID_HOME}"/tools/bin/sdkmanager --licenses \  
&& "${ANDROID_HOME}"/tools/bin/sdkmanager "platform-tools" \  
&& "${ANDROID_HOME}"/tools/bin/sdkmanager "build-tools;26.0.2" \  
&& "${ANDROID_HOME}"/tools/bin/sdkmanager "extras;android;m2repository" \  
&& "${ANDROID_HOME}"/tools/bin/sdkmanager "extras;google;m2repository" \  
&& "${ANDROID_HOME}"/tools/bin/sdkmanager "platforms;android-26"  
  
# Install Gradle  
ENV GRADLE_VERSION=4.4  
RUN wget
https://services.gradle.org/distributions/gradle-"${GRADLE_VERSION}"-all.zip
-q \  
&& mkdir /opt/gradle \  
&& unzip -d /opt/gradle gradle-"${GRADLE_VERSION}"-all.zip \  
&& rm gradle-"${GRADLE_VERSION}"-all.zip  
  
# Setup environment  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tool/tools/bin:${ANDROID_HOME}/platform-
tools:/opt/gradle/gradle-"$GRADLE_VERSION"/bin  
  
# Clear all cache & Delete unused package  
RUN rm -rf /tmp/* /var/cache/apk/*

