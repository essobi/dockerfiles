FROM openjdk:8-alpine  
MAINTAINER HaoHu <haohu.th@gmail.com>  
  
ENV SDK_TOOLS "3859397"  
ENV BUILD_TOOLS "26.0.2"  
ENV TARGET_SDK "26"  
ENV ANDROID_HOME "/opt/android_sdk"  
ENV GLIBC_VERSION "2.26-r0"  
ENV GRADLE_VERSION "4.5"  
ENV GRADLE_HOME "/opt/gradle"  
ENV PATH
"${PATH}:${GRADLE_HOME}/gradle-${GRADLE_VERSION}/bin:${ANDROID_HOME}/bin"  
# Install required dependencies  
RUN apk add --no-cache --virtual=.build-dependencies wget unzip ca-
certificates bash && \  
wget https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub -O /etc/apk/keys/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk -O
/tmp/glibc.apk && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk -O
/tmp/glibc-bin.apk && \  
apk add --no-cache /tmp/glibc.apk /tmp/glibc-bin.apk && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*  
  
# Download and extract Android Tools  
RUN wget http://dl.google.com/android/repository/sdk-tools-
linux-${SDK_TOOLS}.zip -O /tmp/tools.zip && \  
mkdir -p ${ANDROID_HOME} && \  
unzip /tmp/tools.zip -d ${ANDROID_HOME} && \  
rm -v /tmp/tools.zip  
  
# Install SDK Packages  
RUN mkdir -p ${ANDROID_HOME}/licenses/ && \  
echo "\nd56f5187479451eabf01fb78af6dfcb131a6481e" >
${ANDROID_HOME}/licenses/android-sdk-license && \  
echo "\n84831b9409646a918e30573bab4c9c91346d8abd" >
${ANDROID_HOME}/licenses/android-sdk-preview-license && \  
mkdir -p /root/.android/ && touch /root/.android/repositories.cfg && \  
cd /root/.android && \  
yes | ${ANDROID_HOME}/tools/bin/sdkmanager --update && \  
${ANDROID_HOME}/tools/bin/sdkmanager "build-tools;${BUILD_TOOLS}" "platform-
tools" "platforms;android-${TARGET_SDK}" "extras;android;m2repository"
"extras;google;google_play_services" "extras;google;m2repository" && \  
yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses  
  
# Install Gradle  
RUN mkdir -p ${GRADLE_HOME} && \  
wget http://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip
-O /tmp/gradle.zip && \  
unzip /tmp/gradle.zip -d ${GRADLE_HOME} && \  
rm -v /tmp/gradle.zip  
  
RUN mkdir -p /gradle_project  
VOLUME /gradle_project  
WORKDIR /gradle_project  
ENV CLICOLOR 1  
ENV PS1 "\\[\033[01;33m\\]\u@alpine-android\\[\033[01;31m\\]
\W\$\\[\033[00m\\] "  
CMD ["/bin/bash"]  

