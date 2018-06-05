FROM futurenda/buildpack:v1.19.0  
# openjdk:8  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
unzip \  
xz-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'deb http://deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -t jessie-backports -y \  
openjdk-8-jdk \  
ca-certificates-java \  
&& rm -rf /var/lib/apt/lists/* \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
# For running 32 bit Android tools  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
RUN mkdir -p $ANDROID_HOME  
  
# Android SDK Tools 26.1.1  
RUN wget -q https://dl.google.com/android/repository/sdk-tools-
linux-4333796.zip -O /opt/tools.zip \  
&& unzip /opt/tools.zip -d $ANDROID_HOME \  
&& rm -f /opt/tools.zip  
  
RUN yes | sdkmanager 'build-tools;27.0.3' 'extras;google;m2repository'
'platform-tools' 'platforms;android-27' 'tools'  

