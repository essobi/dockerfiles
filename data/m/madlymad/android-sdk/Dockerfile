FROM openjdk:8-slim  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Everything will be installed in the directory but jdk.  
ENV SDK_HOME /usr/local  
  
#Prerequistic packages libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1
libbz2-1.0:i386  
RUN \  
dpkg --add-architecture i386 && \  
apt-get -qq update && \  
apt-get install -qqy --no-install-recommends \  
curl \  
libc6:i386 \  
libncurses5:i386 \  
libstdc++6:i386 \  
lib32z1 \  
libbz2-1.0:i386 \  
&& \  
rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/var/cache/apt/archives/* \  
/var/cache/debconf/*-old  
  
ENV ANDROID_HOME "${SDK_HOME}/sdk"  
ENV PATH "$PATH:${ANDROID_HOME}/tools"  
ENV VERSION_BUILD_TOOLS "27.0.3"  
ENV VERSION_TARGET_SDK "27"  
# https://developer.android.com/studio/index.html#command-tools  
ENV ANDROID_TOOLS_URL http://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip  
  
RUN curl -L "${ANDROID_TOOLS_URL}" -o tools.zip && \  
unzip /tools.zip -d ${ANDROID_HOME} && \  
rm -vrf /tools.zip && \  
rm -vrf \  
${ANDROID_HOME}/tools/monitor-* \  
${ANDROID_HOME}/tools/proguard/examples \  
${ANDROID_HOME}/tools/proguard/docs \  
${ANDROID_HOME}/tools/templates \  
${ANDROID_HOME}/tools/apps  
  
ENV SDK_PACKAGES "build-tools;${VERSION_BUILD_TOOLS}" \  
"extras;android;m2repository" \  
"extras;google;m2repository" \  
"platform-tools" \  
"platforms;android-${VERSION_TARGET_SDK}" \  
"tools"  
RUN mkdir ~/.android  
RUN echo "count=0" > ~/.android/repositories.cfg  
  
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses  
  
RUN (while [ 1 ]; do sleep 5; echo y; done) | \  
${ANDROID_HOME}/tools/bin/sdkmanager ${SDK_PACKAGES} \  
&& \  
rm -vrf `find -type d -name docs` && \  
rm -vrf `find -type d -name templates` && \  
rm -vrf `find -type d -name examples` && \  
rm -vrf `find -type f -name *-javadoc.jar*`

