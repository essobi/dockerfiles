FROM ubuntu:16.04  
MAINTAINER koperko  
  
ENV VERSION_BUILD_TOOLS "26.0.0"  
ENV VERSION_TARGET_SDK "26"  
ENV ANDROID_HOME "/sdk"  
ENV PATH "$PATH:${ANDROID_HOME}/tools"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update && \  
apt-get install -qqy --no-install-recommends \  
curl \  
html2text \  
openjdk-8-jdk \  
libc6-i386 \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
unzip \  
git \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN rm -f /etc/ssl/certs/java/cacerts; \  
/var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
ADD https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
/tools.zip  
RUN unzip /tools.zip -d /sdk && \  
rm -v /tools.zip  
  
RUN echo y | /sdk/tools/bin/sdkmanager "platforms;android-26"  
RUN echo y | /sdk/tools/bin/sdkmanager "platform-tools"  
RUN echo y | /sdk/tools/bin/sdkmanager "build-tools;26.0.0"  
RUN echo y | /sdk/tools/bin/sdkmanager "extras;android;m2repository"  
RUN echo y | /sdk/tools/bin/sdkmanager "extras;google;m2repository"  
RUN echo y | /sdk/tools/bin/sdkmanager "extras;google;google_play_services"  

