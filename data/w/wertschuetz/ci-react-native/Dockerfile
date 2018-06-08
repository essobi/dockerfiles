FROM mhart/alpine-node:8  
  
ENV LANG C.UTF-8  
ENV VERSION_SDK_TOOLS "3859397"  
ENV VERSION_BUILD_TOOLS "25.0.5"  
ENV VERSION_TARGET_SDK "25  
ENV SDK_PACKAGES "build-
tools-${VERSION_BUILD_TOOLS},android-${VERSION_TARGET_SDK},platform-
tools,extra-android-m2repository,extra-google-google_play_services,extra-
google-m2repository"  
ENV ANDROID_HOME "/opt/android-sdk-linux"  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
ENV GLIBC_VERSION "2.25-r0"  
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:${ANDROID_HOME}/tools/lib64  
  
RUN set -x \  
&& apk add \--no-cache git maven bash iperf curl wget openssh openjdk8  
  
#------------Installing Glibc
Packages----------------------------------------------------------------  
  
RUN apk add \--no-cache --virtual=.build-dependencies wget unzip ca-
certificates && \  
wget https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub -O /etc/apk/keys/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_VERSION/glibc-$GLIBC_VERSION.apk -O
/tmp/glibc.apk && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_VERSION/glibc-bin-$GLIBC_VERSION.apk -O
/tmp/glibc-bin.apk && \  
apk add \--no-cache /tmp/glibc.apk /tmp/glibc-bin.apk && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*  
  
# Download and extract Android Tools  
RUN wget http://dl.google.com/android/repository/sdk-tools-
linux-${VERSION_SDK_TOOLS}.zip -O /tmp/tools.zip && \  
mkdir -p $ANDROID_HOME && \  
unzip /tmp/tools.zip -d $ANDROID_HOME && \  
rm -v /tmp/tools.zip  
  
# Install SDK Packages  
RUN echo y | sdkmanager 'tools' \  
&& sdkmanager 'platform-tools' \  
&& sdkmanager "platforms;android-26" \  
&& sdkmanager "platforms;android-25" \  
&& sdkmanager "platforms;android-23" \  
&& sdkmanager "build-tools;26.0.0" \  
&& sdkmanager "build-tools;25.0.3" \  
&& sdkmanager "build-tools;23.0.1" \  
&& sdkmanager "add-ons;addon-google_apis-google-24" \  
&& sdkmanager "add-ons;addon-google_apis-google-16"  
  
WORKDIR "/var/lib/build/workspace"  
  
CMD ["/bin/sh"]  
  

