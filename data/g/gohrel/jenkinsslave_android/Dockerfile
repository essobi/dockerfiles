############################################################  
# Dockerfile to build jenkins swarm slaves container images that can handle
android builds  
# Based on openjdk:9  
############################################################  
FROM openjdk:9  
MAINTAINER Holger Zunker <holger50@gmx.de>  
  
# Create a non-root user  
RUN useradd -m user  
WORKDIR /home/user  
  
# Install Git and dependencies  
USER root  
RUN dpkg --add-architecture i386 && apt-get update && apt-get -y upgrade &&
apt-get install -y --force-yes file curl libncurses5:i386 libstdc++6:i386
zlib1g:i386 expect libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 git
unzip && apt-get clean  
  
USER user  
# Install Gradle  
ENV GRADLE_VERSION="4.7"  
ENV
GRADLE_URL="https://downloads.gradle.org/distributions/gradle-$GRADLE_VERSION-
all.zip"  
#ENV
GRADLE_URL="https://service.gradle.org/distributions/gradle-$GRADLE_VERSION-
all.zip"  
RUN curl {$GRADLE_URL} -o gradle.zip  
RUN unzip -q gradle.zip  
RUN mv gradle-$GRADLE_VERSION gradle  
RUN rm gradle.zip  
RUN mkdir .gradle  
  
# Install Android tools  
# Download Android SDK  
#ENV BUILD_TOOLS_VERSION 27.0.3  
#ENV ANDROID_VERSION 25  
ENV SDK_VERSION="sdk-tools-linux-3859397.zip"  
ENV ANDROID_HOME="/home/user/android-sdk-linux"  
ENV SDK_URL="https://dl.google.com/android/repository/{$SDK_VERSION}"  
ENV
PATH="/home/user/gradle/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:${ANDROID_HOME}/tools/bin:${PATH}"  
USER root  
COPY scripts/android-accept-licenses.sh /home/user/scripts/  
RUN chmod 755 /home/user/scripts/*  
RUN mkdir -p "$ANDROID_HOME" && cd "$ANDROID_HOME"  
RUN curl -o tools-sdk.zip
https://dl.google.com/android/repository/$SDK_VERSION  
RUN unzip tools-sdk.zip -d $ANDROID_HOME/  
RUN rm -f tools-sdk.zip  
  
RUN chmod -R 755 $ANDROID_HOME/* && chown -R user:user $ANDROID_HOME/*  
COPY licenses /home/user/android-sdk-linux/licenses  
RUN /home/user/scripts/android-accept-licenses.sh
"$ANDROID_HOME/tools/bin/sdkmanager platform-tools \"build-
tools;${BUILD_TOOLS_VERSION}\" \"platforms;android-${ANDROID_VERSION}\" \"add-
ons;addon-google_apis-google-24\"
\"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2\"
\"extras;m2repository;com;android;support;constraint;constraint-layout-
solver;1.0.2\" \"system-
images;android-${ANDROID_VERSION};google_apis;armeabi-v7a\" ndk-bundle"  
  
#Install Jenkins dependencies  
ENV JENKINS_MASTER_USERNAME="jenkins" \  
JENKINS_MASTER_PASSWORD="jenkins" \  
JENKINS_MASTER_URL="http://jenkins:8080/" \  
JENKINS_SLAVE_MODE="exclusive" \  
JENKINS_SLAVE_NAME="Android" \  
JENKINS_SLAVE_WORKERS="1" \  
JENKINS_SLAVE_LABELS="Android java9 openjdk9 gradle" \  
AVD=""  
ENV JENKINS_SLAVE_ROOT="/home/user/"  
ENV HOME=/home/user \  
JENKINS_SWARM_VERSION=3.9 \  
JENKINS_SWARM_JAR_PATH=/home/user  
ENV JENKINS_SWARM_JAR=${JENKINS_SWARM_JAR_PATH}/swarm.jar  
COPY scripts/entrypoint.sh /home/user/scripts/  
  
RUN mkdir -p "$JENKINS_SLAVE_ROOT"  
# Install Jenkins slave (swarm)  
RUN mkdir -p $JENKINS_SWARM_JAR_PATH \  
&& chmod 755 $JENKINS_SWARM_JAR_PATH \  
&& curl -SLo $JENKINS_SWARM_JAR http://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION.jar  
  
#ADD entrypoint.sh /usr/bin/  
USER root  
RUN chmod +x /home/user/scripts/entrypoint.sh  
RUN chown -R user:user /home/user/scripts/*  
ENTRYPOINT /home/user/scripts/entrypoint.sh  
  
RUN mkdir $ANDROID_HOME/ndk-bundle  
RUN chmod -R 777 $ANDROID_HOME/ && chown -R user:user $ANDROID_HOME  
  
USER user  
VOLUME ${HOME}  
WORKDIR ${HOME}  
  

