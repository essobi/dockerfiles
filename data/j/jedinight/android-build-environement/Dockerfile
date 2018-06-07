# Android Dockerfile  
FROM ubuntu:16.04  
MAINTAINER Mobile Builds Eng "jp.tessier.dev@gmail.com"  
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
  
# Download JDK 8 Oracle  
#RUN wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u111-b14/jdk-8u111-linux-x64.tar.gz  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u112-b15/jdk-8u112-linux-x64.tar.gz  
RUN tar -xvzf jdk-8u112-linux-x64.tar.gz  
# Install JDK 8 Oracle  
RUN mv jdk1.8.0_112 /usr/local/java  
  
# Export JAVA_HOME variable  
ENV JAVA_HOME /usr/local/java  
ENV PATH $PATH:$JAVA_HOME/bin  
  
# Cleanup JDK 8 tar.gz  
RUN rm jdk-8u112-linux-x64.tar.gz  
  
# Clean Up Apt-get  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get clean  
  
# Install Android SDK 24  
RUN wget https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz  
RUN tar -xvzf android-sdk_r24.4.1-linux.tgz  
RUN mv android-sdk-linux /usr/local/android-sdk  
RUN rm android-sdk_r24.4.1-linux.tgz  
  
# Prepare components Android to version 25  
ENV ANDROID_COMPONENTS platform-tools-25.0.0,android-25,build-
tools-25.0.0,extra-android-support,extra-android-m2repository,extra-
google-m2repository  
  
# Update Android componentes and accept licence  
RUN echo y | /usr/local/android-sdk/tools/android update sdk --no-ui -a
--filter "${ANDROID_COMPONENTS}"  
  
# Install Android NDK r13  
RUN wget http://dl.google.com/android/repository/android-
ndk-r13-linux-x86_64.zip  
RUN unzip android-ndk-r13-linux-x86_64.zip  
RUN mv android-ndk-r13 /usr/local/android-ndk  
RUN rm android-ndk-r13-linux-x86_64.zip  
  
# Environment variables  
ENV ANDROID_HOME /usr/local/android-sdk  
ENV ANDROID_SDK_HOME $ANDROID_HOME  
ENV ANDROID_NDK_HOME /usr/local/android-ndk  
ENV JENKINS_HOME $HOME  
ENV PATH ${INFER_HOME}/bin:${PATH}  
ENV PATH $PATH:$ANDROID_SDK_HOME/tools  
ENV PATH $PATH:$ANDROID_SDK_HOME/platform-tools  
ENV PATH $PATH:$ANDROID_SDK_HOME/build-tools/25.0.0  
ENV PATH $PATH:$ANDROID_NDK_HOME  
  
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

