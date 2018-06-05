# Inspired from https://github.com/heikomaass/docker-
android/blob/master/android-sdk/Dockerfile  
FROM node:6  
MAINTAINER Fabian Köster <fabian.koester@bringnow.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
RUN bash -c "echo deb http://ftp.debian.org/debian jessie-backports main >>
/etc/apt/sources.list" \  
&& dpkg --add-architecture i386 \  
&& apt-get update && apt-get install -t jessie-backports -y \--no-install-
recommends openjdk-8-jdk-headless \  
expect \  
libncurses5:i386 \  
libstdc++6:i386 \  
zlib1g:i386 \  
build-essential \  
openssh-client \  
&& apt-get install -y \--no-install-recommends maven \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Android SDK installer  
ARG ANDROID_SDK_BUILD=3859397  
ARG
ANDROID_SDK_SHA256=444e22ce8ca0f67353bda4b85175ed3731cae3ffa695ca18119cbacef1c1bea0  
RUN curl -o android-sdk.zip "https://dl.google.com/android/repository/sdk-
tools-linux-${ANDROID_SDK_BUILD}.zip" \  
&& echo "${ANDROID_SDK_SHA256} android-sdk.zip" | sha256sum -c \  
&& unzip -C android-sdk.zip -d "${ANDROID_HOME}" \  
&& rm *.zip  
  
COPY tools /opt/sdk-tools  
  
ENV PATH
${PATH}:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:/opt/sdk-tools  
  
RUN sdkmanager --list \  
&& /opt/sdk-tools/android-accept-licenses.sh "sdkmanager --update" \  
&& /opt/sdk-tools/android-accept-licenses.sh "sdkmanager build-tools;23.0.3" \  
&& /opt/sdk-tools/android-accept-licenses.sh "sdkmanager build-tools;24.0.3" \  
&& /opt/sdk-tools/android-accept-licenses.sh "sdkmanager build-tools;25.0.3" \  
&& /opt/sdk-tools/android-accept-licenses.sh "sdkmanager build-tools;26.0.2" \  
&& /opt/sdk-tools/android-accept-licenses.sh "sdkmanager build-tools;27.0.0" \  
&& /opt/sdk-tools/android-accept-licenses.sh "sdkmanager sources;android-23" \  
&& /opt/sdk-tools/android-accept-licenses.sh "sdkmanager sources;android-24" \  
&& /opt/sdk-tools/android-accept-licenses.sh "sdkmanager sources;android-25" \  
&& /opt/sdk-tools/android-accept-licenses.sh "sdkmanager sources;android-26" \  
&& /opt/sdk-tools/android-accept-licenses.sh "sdkmanager sources;android-27" \  
&& sdkmanager --list  

