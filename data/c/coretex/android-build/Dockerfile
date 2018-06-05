FROM ubuntu:14.04  
RUN \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
-a /etc/apt/sources.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && apt-get
update && apt-get install -y oracle-java8-installer ca-certificates && \  
dpkg --add-architecture i386 && apt-get update && apt-get install -y --force-
yes expect git wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1
python curl unzip && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Install Android SDK  
RUN \  
cd /opt && mkdir android-sdk-linux && cd android-sdk-linux && wget --output-
document=android-sdk.zip --quiet https://dl.google.com/android/repository/sdk-
tools-linux-3859397.zip && unzip android-sdk.zip && rm -f android-sdk.zip &&
cd .. && chown -R root.root android-sdk-linux  
  
# Setup environment  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
# Install sdk elements  
COPY tools /opt/tools  
ENV PATH ${PATH}:/opt/tools  
RUN chmod +x /opt/tools/*  
  
ENV TOOLS_VERSION 26.0.2  
ENV PLATFORM_VERSION 25  
RUN echo "android-${PLATFORM_VERSION} tools-${TOOLS_VERSION}"  
  
RUN yes | /opt/android-sdk-linux/tools/bin/sdkmanager --licenses  
  
RUN opt/android-sdk-linux/tools/bin/sdkmanager "platform-tools" "build-
tools;25.0.1" "build-tools;$TOOLS_VERSION" "platforms;android-26"
"platforms;android-$PLATFORM_VERSION" "extras;android;m2repository"
"extras;google;m2repository" "extras;google;google_play_services"  
  
ENV BUILD_TOOLS ${ANDROID_HOME}/build-tools/${TOOLS_VERSION}  
  
RUN which adb  
RUN which android  
  
# Setup scripting bonuses  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install requests  
  
# Cleaning  
RUN apt-get clean  
  
# add constraint-layout beta-4  
COPY m2repository $ANDROID_HOME/extras/m2repository/  
  
# GO to workspace  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace

