FROM ubuntu:17.04  
# Install library  
RUN apt-get update && apt-get install -y software-properties-common  
RUN dpkg --add-architecture i386 && apt-get update && \  
apt-get install -y locales ca-certificates vim rsync sudo zip git build-
essential wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 python
curl psmisc module-init-tools python-pip && \  
apt-get clean  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
RUN mkdir -p /opt  
WORKDIR /opt  
  
# Setup environment  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
ENV JAVA_VERSION 1.8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/  
  
# Install java 8  
RUN add-apt-repository -y ppa:webupd8team/java && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get update && \  
apt-get install -y --no-install-recommends oracle-java8-installer && \  
apt-get install -y --no-install-recommends oracle-java8-set-default && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Install android sdk for linux  
# Check this website for more information :
https://developer.android.com/studio/index.html  
RUN wget --output-document=android-sdk.zip --quiet
https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \  
mkdir /opt/android-sdk-linux && \  
unzip android-sdk.zip -d /opt/android-sdk-linux && \  
rm -f android-sdk.zip  
RUN mkdir ~/.android && touch ~/.android/repositories.cfg  
  
# Install android sdk packages  
# Check this website for more information :
https://developer.android.com/studio/command-line/sdkmanager.html  
RUN yes | sdkmanager --licenses  
RUN sdkmanager "build-tools;27.0.2"  
RUN sdkmanager "platform-tools"  
RUN sdkmanager "tools"  
RUN sdkmanager "extras;android;m2repository"  
RUN sdkmanager "extras;google;m2repository"  
RUN sdkmanager "extras;google;google_play_services"  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout;1.0.2"  
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-
layout-solver;1.0.2"  
RUN sdkmanager "platforms;android-25"  
RUN sdkmanager "platforms;android-26"  
RUN sdkmanager "platforms;android-27"  
RUN sdkmanager "patcher;v4"  
RUN sdkmanager --update  
RUN yes | sdkmanager --licenses  
  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace

