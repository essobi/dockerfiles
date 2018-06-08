FROM pondthaitay/java-build-android  
  
LABEL MAINTAINER Jedsada Tiwongvorakul <pondthaitay@gmail.com>  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV GRADLE_VERSION 4.4  
  
ENV ANDROID_SDK_URL="https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip" \  
ANDROID_BUILD_TOOLS_VERSION=27 \  
ANDROID_APIS="android-26" \  
ANT_HOME="/usr/share/ant" \  
MAVEN_HOME="/usr/share/maven" \  
GRADLE_URL="https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip"
\  
ANDROID_HOME="/opt/android-sdk-linux"  
# Install Android SDK  
RUN cd /opt \  
&& wget -q ${ANDROID_SDK_URL} -O android-sdk-tools.zip \  
&& unzip -q android-sdk-tools.zip -d ${ANDROID_HOME} \  
&& rm android-sdk-tools.zip  
  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
RUN yes | sdkmanager --licenses  
  
# Platform tools  
RUN sdkmanager "emulator" "tools" "platform-tools"  
RUN yes | sdkmanager \  
"platforms;android-27" \  
"build-tools;27.0.3" \  
"extras;android;m2repository" \  
"extras;google;m2repository" \  
"extras;google;google_play_services" \  
"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2" \  
"extras;m2repository;com;android;support;constraint;constraint-layout-
solver;1.0.2"  
RUN echo "sdk.dir=$ANDROID_HOME" > local.properties  
  
# Install Gradle  
ENV SDK_HOME /otp  
RUN curl -sSL "${GRADLE_URL}" -o gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip gradle-${GRADLE_VERSION}-bin.zip -d ${SDK_HOME} \  
&& rm -rf gradle-${GRADLE_VERSION}-bin.zip  
ENV GRADLE_HOME ${SDK_HOME}/gradle-${GRADLE_VERSION}  
ENV PATH ${GRADLE_HOME}/bin:$PATH  
# Cleaning  
RUN apt-get clean

