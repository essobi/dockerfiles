# FROM jacekmarchwicki/android:latest  
# FROM uber/android-build-environment:latest  
FROM ubuntu:14.04  
MAINTAINER Aiden Montgomery "aiden@constructivecoding.com"  
# Sets language to UTF8 : this works in pretty much all cases  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
  
ENV DOCKER_ANDROID_LANG en_US  
ENV DOCKER_ANDROID_DISPLAY_NAME mobileci-docker  
  
# Never ask for confirmations  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update apt-get  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
  
# Installing packages  
RUN apt-get install -y \  
autoconf \  
build-essential \  
bzip2 \  
curl \  
gcc \  
git \  
groff \  
lib32stdc++6 \  
lib32z1 \  
lib32z1-dev \  
lib32ncurses5 \  
lib32bz2-1.0 \  
libc6-dev \  
libgmp-dev \  
libmpc-dev \  
libmpfr-dev \  
libxslt-dev \  
libxml2-dev \  
m4 \  
make \  
ncurses-dev \  
ocaml \  
openssh-client \  
pkg-config \  
python-software-properties \  
rsync \  
software-properties-common \  
unzip \  
wget \  
zip \  
zlib1g-dev \  
\--no-install-recommends  
  
# Install Java  
RUN apt-add-repository ppa:openjdk-r/ppa  
RUN apt-get update  
RUN apt-get -y install openjdk-8-jdk  
  
# Clean Up Apt-get  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get clean  
  
# Install Android SDK  
RUN wget https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz  
RUN tar -xvzf android-sdk_r24.4.1-linux.tgz  
RUN mv android-sdk-linux /usr/local/android-sdk  
RUN rm android-sdk_r24.4.1-linux.tgz  
  
ENV ANDROID_COMPONENTS platform-tools,tools,build-tools-23.0.1,build-
tools-23.0.2,android-23,addon-google_apis_x86-google-21,extra-android-
support,extra-android-m2repository,extra-google-m2repository,extra-google-
google_play_services,sys-img-armeabi-v7a-android-23  
# Install Android tools  
RUN echo y | /usr/local/android-sdk/tools/android update sdk --filter
"platform-tools,tools,build-tools-23.0.1,build-tools-23.0.2,android-23,addon-
google_apis_x86-google-21,extra-android-support,extra-
android-m2repository,extra-google-m2repository,extra-google-
google_play_services,sys-img-armeabi-v7a-android-23" \--no-ui -a  
  
# Install Android NDK  
RUN wget http://dl.google.com/android/repository/android-
ndk-r12-linux-x86_64.zip  
RUN unzip android-ndk-r12-linux-x86_64.zip  
RUN mv android-ndk-r12 /usr/local/android-ndk  
RUN rm android-ndk-r12-linux-x86_64.zip  
  
# Environment variables  
ENV ANDROID_HOME /usr/local/android-sdk  
ENV ANDROID_SDK_HOME $ANDROID_HOME  
ENV ANDROID_NDK_HOME /usr/local/android-ndk  
ENV JENKINS_HOME $HOME  
ENV PATH ${INFER_HOME}/bin:${PATH}  
ENV PATH $PATH:$ANDROID_SDK_HOME/tools  
ENV PATH $PATH:$ANDROID_SDK_HOME/platform-tools  
ENV PATH $PATH:$ANDROID_SDK_HOME/build-tools/23.0.2  
ENV PATH $PATH:$ANDROID_SDK_HOME/build-tools/23.0.1  
ENV PATH $PATH:$ANDROID_NDK_HOME  
  
# Export JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
  
# Support Gradle  
ENV TERM dumb  
ENV JAVA_OPTS "-Xms4096m -Xmx4096m"  
ENV GRADLE_OPTS "-XX:+UseG1GC -XX:MaxGCPauseMillis=1000"  
# Cleaning  
RUN apt-get clean  
  
# Add build user account, values are set to default below  
ENV RUN_USER mobileci  
ENV RUN_UID 5089  
RUN id $RUN_USER || adduser --uid "$RUN_UID" \  
\--gecos 'Build User' \  
\--shell '/bin/sh' \  
\--disabled-login \  
\--disabled-password "$RUN_USER"  
  
# Fix permissions  
RUN chown -R $RUN_USER:$RUN_USER $ANDROID_HOME $ANDROID_SDK_HOME
$ANDROID_NDK_HOME  
RUN chmod -R a+rx $ANDROID_HOME $ANDROID_SDK_HOME $ANDROID_NDK_HOME  
  
# Creating project directories prepared for build when running  
# `docker run`  
ENV PROJECT /project  
RUN mkdir $PROJECT  
RUN chown -R $RUN_USER:$RUN_USER $PROJECT  
WORKDIR $PROJECT  
  
USER $RUN_USER  
RUN echo "sdk.dir=$ANDROID_HOME" > local.properties  

