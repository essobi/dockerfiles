# Android Dockerfile  
FROM ubuntu:14.04  
MAINTAINER Mobile Builds Eng "paul.riley@mnscorp.net"  
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
dos2unix \  
\--no-install-recommends  
  
# Install Java  
RUN apt-get update  
RUN apt-add-repository ppa:webupd8team/java  
RUN apt-get update  
  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo
debconf-set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-
set-selections  
  
RUN apt-get -y install oracle-java8-installer oracle-java8-set-default  
  
# Clean Up Apt-get  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get clean  
  
# Environment variables  
ENV ANDROID_HOME /usr/local/android-sdk  
ENV ANDROID_SDK_HOME $ANDROID_HOME  
ENV ANDROID_NDK_HOME /usr/local/android-ndk  
ENV JENKINS_HOME $HOME  
ENV PATH ${INFER_HOME}/bin:${PATH}  
ENV PATH $PATH:$ANDROID_SDK_HOME/tools  
ENV PATH $PATH:$ANDROID_SDK_HOME/platform-tools  
ENV PATH $PATH:$ANDROID_SDK_HOME/build-tools/27.0.3  
ENV PATH $PATH:$ANDROID_NDK_HOME  
ENV ANDROID_SDK_PACKAGES="build-tools;27.0.3 platforms;android-27 platform-
tools extras;android;m2repository extras;google;m2repository
extras;google;google_play_services"  
# Install Android SDK  
RUN wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
-O /tmp/android-tools.zip && \  
unzip /tmp/android-tools.zip -d ${ANDROID_HOME} && \  
rm -v /tmp/android-tools.zip  
  
# Install Android SDK Packages  
# https://developer.android.com/studio/command-line/sdkmanager.html  
RUN mkdir -p ${ANDROID_HOME}/licenses/  
RUN echo "8933bad161af4178b1185d1a37fbf41ea5269c55" >
${ANDROID_HOME}/licenses/android-sdk-license  
RUN echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >>
${ANDROID_HOME}/licenses/android-sdk-license  
RUN echo "84831b9409646a918e30573bab4c9c91346d8abd" >
${ANDROID_HOME}/licenses/android-sdk-preview-license  
RUN chmod +x ${ANDROID_HOME}/tools/bin/sdkmanager  
RUN touch /usr/local/share/android-sdk  
RUN ${ANDROID_HOME}/tools/bin/sdkmanager --channel=3 --verbose
${ANDROID_SDK_PACKAGES}  
  
# Install Android NDK  
RUN wget http://dl.google.com/android/repository/android-
ndk-r15b-linux-x86_64.zip -O /tmp/android-ndk.zip  
RUN unzip /tmp/android-ndk.zip -d ${ANDROID_NDK_HOME}  
RUN rm -v /tmp/android-ndk.zip  
  
# Export JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/  
  
# Support Gradle  
ENV TERM dumb  
ENV JAVA_OPTS "-Xms512m -Xmx1024m"  
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

