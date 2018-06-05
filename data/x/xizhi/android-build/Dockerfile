FROM openjdk:8-jdk  
MAINTAINER author="Xizhi Xu" email="xizhi.xu@outlook.com" version="0.1"
decription="This is a docker image for android build"  
ENV VERSION_SDK_TOOLS "3859397"  
ENV ANDROID_HOME /android-sdk  
ENV PATH
$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools  
ENV DEBIAN_FRONTEND noninteractive  
  
# Gradle props  
ENV JAVA_OPTS "-Xms1g -Xmx4g"  
ENV GRADLE_OPTS "-XX:+UseG1GC -XX:MaxGCPauseMillis=1000"  
# Install tools  
RUN apt-get -qq update && \  
apt-get install -qqy --no-install-recommends \  
git-all \  
curl \  
wget \  
unzip \  
lib32stdc++6 \  
lib32z1 \  
jq \  
python-pip  
  
# Clean up  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get clean  
  
# Android sdk tools  
ADD https://dl.google.com/android/repository/sdk-tools-
linux-${VERSION_SDK_TOOLS}.zip /sdk.zip  
RUN unzip /sdk.zip -d ${ANDROID_HOME} && \  
rm -v /sdk.zip  
  
# Agreements  
RUN mkdir -p $ANDROID_HOME/licenses/ \  
&& echo
"8933bad161af4178b1185d1a37fbf41ea5269c55\nd56f5187479451eabf01fb78af6dfcb131a6481e"
> $ANDROID_HOME/licenses/android-sdk-license \  
&& echo "84831b9409646a918e30573bab4c9c91346d8abd" >
$ANDROID_HOME/licenses/android-sdk-preview-license  
  
# Install sdk  
ADD packages ${ANDROID_HOME}  
RUN mkdir -p /root/.android && \  
touch /root/.android/repositories.cfg && \  
sdkmanager --update && \  
(while [ 1 ]; do sleep 5; echo y; done) | cat $ANDROID_HOME/packages | xargs
sdkmanager --verbose  

