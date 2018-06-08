# Android Dockerfile  
FROM ubuntu:14.04  
# Source :  
# https://github.com/uber-common/android-build-environment/  
# Improving size with  
# https://github.com/uber-common/android-build-
environment/pull/13/commits/a13dd1f99ae614b6fbe363310a8cb4b55dcecd46  
# Sets language to UTF8 : this works in pretty much all cases  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
  
ENV DOCKER_ANDROID_LANG en_US  
ENV DOCKER_ANDROID_DISPLAY_NAME mobileci-docker  
  
# Never ask for confirmations  
ENV DEBIAN_FRONTEND noninteractive  
  
# Updating & Installing packages  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y \  
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
\--no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Java  
RUN apt-add-repository ppa:openjdk-r/ppa \  
&& apt-get update \  
&& apt-get -y install openjdk-8-jdk \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Environment variables  
ENV ANDROID_HOME /usr/local/android-sdk  
ENV ANDROID_SDK_HOME $ANDROID_HOME  
ENV ANDROID_NDK_HOME /usr/local/android-ndk  
ENV PATH ${INFER_HOME}/bin:${PATH}  
ENV PATH $PATH:$ANDROID_SDK_HOME/tools  
ENV PATH $PATH:$ANDROID_SDK_HOME/platform-tools  
ENV PATH $PATH:$ANDROID_SDK_HOME/build-tools/23.0.2  
ENV PATH $PATH:$ANDROID_SDK_HOME/build-tools/24.0.0  
ENV PATH $PATH:$ANDROID_NDK_HOME  
  
# Export JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
  
# Support Gradle  
ENV TERM dumb  
ENV JAVA_OPTS "-Xms4096m -Xmx4096m"  
ENV GRADLE_OPTS "-XX:+UseG1GC -XX:MaxGCPauseMillis=1000"  
# Pre-install gradle for faster builds.  
ENV GRADLE_VERSION 3.3  
WORKDIR /usr/bin  
RUN wget
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"
&& \  
unzip "gradle-${GRADLE_VERSION}-bin.zip" && \  
ln -s "gradle-${GRADLE_VERSION}" gradle && \  
rm "gradle-${GRADLE_VERSION}-bin.zip"  
  
ENV GRADLE_HOME /usr/bin/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
  
# Cleaning  
RUN apt-get clean  
  
# Add build user account, values are set to default below  
ENV RUN_USER mobileci  
ENV RUN_UID 1000  
RUN id $RUN_USER || adduser --uid "$RUN_UID" \  
\--gecos 'Build User' \  
\--shell '/bin/sh' \  
\--disabled-login \  
\--disabled-password "$RUN_USER"  
  
# Install Android SDK  
RUN wget https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz \  
&& tar -xvzf android-sdk_r24.4.1-linux.tgz \  
&& mv android-sdk-linux $ANDROID_HOME \  
&& chown -R $RUN_USER:$RUN_USER $ANDROID_HOME \  
&& chmod -R a+rx $ANDROID_HOME \  
&& rm android-sdk_r24.4.1-linux.tgz \  
&& mkdir $ANDROID_HOME/licenses \  
&& echo "8933bad161af4178b1185d1a37fbf41ea5269c55" >
$ANDROID_HOME/licenses/android-sdk-license  
  
ENV ANDROID_COMPONENTS platform-tools,android-23,build-tools-23.0.2,build-
tools-24.0.0  
# Install Android tools  
RUN echo y | /usr/local/android-sdk/tools/android update sdk --filter
"${ANDROID_COMPONENTS}" \--no-ui -a \  
&& chown -R $RUN_USER:$RUN_USER $ANDROID_HOME \  
&& chmod -R a+rx $ANDROID_HOME  
  
# Install Android NDK  
RUN wget http://dl.google.com/android/repository/android-
ndk-r12-linux-x86_64.zip \  
&& unzip android-ndk-r12-linux-x86_64.zip \  
&& mv android-ndk-r12 /usr/local/android-ndk \  
&& chown -R $RUN_USER:$RUN_USER $ANDROID_NDK_HOME \  
&& chmod -R a+rx $ANDROID_NDK_HOME \  
&& rm android-ndk-r12-linux-x86_64.zip  
  
### INSTALL NODE  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.11.1  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
### INSTALL ANGULAR/CLI AND CORDOVA  
RUN npm install -g @angular/cli@1.2.1 \  
&& npm install -g cordova \  
&& npm install -g firebase-tools \  
&& npm cache clean  
  
EXPOSE 4200  
# Creating project directories prepared for build when running  
# `docker run`  
ENV PROJECT /project  
RUN mkdir $PROJECT && \  
chown -R $RUN_USER:$RUN_USER $PROJECT  
WORKDIR $PROJECT  
  
USER $RUN_USER  
RUN echo "sdk.dir=$ANDROID_HOME" > local.properties  
  
### ALIAS  
RUN echo "alias ll='ls -l'" >> ~/.bashrc \  
&& echo "alias lla='ls _la'" >> ~/.bashrc  
  
# LOAD DEPENDENCIES  
RUN cordova create tmp-project && \  
cd tmp-project && \  
cordova platform add android && \  
cordova build && \  
cd .. && \  
rm -rf tmp-project  

