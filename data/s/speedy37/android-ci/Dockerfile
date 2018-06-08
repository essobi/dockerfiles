#  
# GitLab CI: Android v0.2  
#  
# https://hub.docker.com/r/jangrewe/gitlab-ci-android/  
# https://git.faked.org/jan/gitlab-ci-android  
#  
FROM ubuntu:16.04  
MAINTAINER Vincent Rouillé <v-rouille@logitud.fr>  
  
ENV VERSION_SDK_TOOLS "26.0.2"  
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
/var/lib/dpkg/info/ca-certificates-java.postinst configure \  
&& curl https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip >
/tools.zip \  
&& unzip /tools.zip -d /sdk \  
&& rm -v /tools.zip  
  
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses  
RUN ${ANDROID_HOME}/tools/bin/sdkmanager --update  
RUN ${ANDROID_HOME}/tools/bin/sdkmanager \  
"build-tools;26.0.2" \  
"platforms;android-25" \  
"sources;android-25" \  
"extras;android;m2repository" \  
"extras;google;m2repository" \  

