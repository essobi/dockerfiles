FROM ubuntu:16.04  
MAINTAINER Alexis Duque <alexisd@rtone.fr>  
  
ENV VERSION_SDK_TOOLS "3859397"  
ENV ANDROID_HOME "/sdk"  
ENV SDK_HOME "/opt"  
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
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN rm -f /etc/ssl/certs/java/cacerts; \  
/var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
RUN curl -s https://dl.google.com/android/repository/sdk-tools-
linux-${VERSION_SDK_TOOLS}.zip > /sdk.zip && \  
unzip /sdk.zip -d /sdk && \  
rm -v /sdk.zip  
  
RUN mkdir -p $ANDROID_HOME/licenses/ \  
&& echo "8933bad161af4178b1185d1a37fbf41ea5269c55" >
$ANDROID_HOME/licenses/android-sdk-license \  
&& echo "84831b9409646a918e30573bab4c9c91346d8abd" >
$ANDROID_HOME/licenses/android-sdk-preview-license  
  
# Gradle  
ENV GRADLE_VERSION 4.1  
ENV GRADLE_SDK_URL
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip  
RUN curl -sSL "${GRADLE_SDK_URL}" -o gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip gradle-${GRADLE_VERSION}-bin.zip -d ${SDK_HOME} \  
&& rm -rf gradle-${GRADLE_VERSION}-bin.zip  
ENV GRADLE_HOME ${SDK_HOME}/gradle-${GRADLE_VERSION}  
ENV PATH ${GRADLE_HOME}/bin:$PATH  
  
ADD packages.txt /sdk  
RUN mkdir -p /root/.android && \  
touch /root/.android/repositories.cfg && \  
${ANDROID_HOME}/tools/bin/sdkmanager --update && \  
(while [ 1 ]; do sleep 5; echo y; done) | ${ANDROID_HOME}/tools/bin/sdkmanager
--package_file=/sdk/packages.txt  
  
RUN chmod -R a+rwx ${ANDROID_HOME}  
  

