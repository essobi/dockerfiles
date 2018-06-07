FROM debian:jessie  
LABEL maintainer="gregunz <contact@gregunz.io>"  
  
ENV DEBIAN_FRONTEND=noninteractive \  
ANDROID_HOME=/opt/android-sdk-linux \  
GRADLE_HOME=/opt/gradle \  
GRADLE_VERSION=4.2 \  
NPM_VERSION=5.4.2 \  
IONIC_VERSION=3.12.0 \  
CORDOVA_VERSION=7.0.1 \  
# Fix for the issue with Selenium, as described here:  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
DBUS_SESSION_BUS_ADDRESS=/dev/null  
  
# Install basics  
RUN set -x \  
&& apt-get update && apt-get install -y \  
build-essential \  
curl \  
git \  
python-software-properties \  
ruby \  
ruby-dev \  
software-properties-common \  
unzip \  
wget \  
zip \  
  
# Install Gradle  
&& wget --output-document=gradle-bin.zip
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
&& mkdir ${GRADLE_HOME} \  
&& unzip -d ${GRADLE_HOME} gradle-bin.zip \  
&& ls ${GRADLE_HOME} \  
&& ls ${GRADLE_HOME}/gradle-${GRADLE_VERSION} \  
  
# NODEJS  
# Install nodejs  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get update && apt-get install -y \  
nodejs \  
  
# IONIC & CORDOVA  
# Install depencies (npm, cordova, ionic, yarn, sass, scss_lint)  
&& npm install -g \  
npm@"$NPM_VERSION" \  
cordova@"$CORDOVA_VERSION" \  
ionic@"$IONIC_VERSION" \  
  
&& gem install \  
sass \  
scss_lint \  
  
# Install chrome (for e2e test, headless use)  
&& wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& dpkg --unpack google-chrome-stable_current_amd64.deb \  
&& apt-get install -f -y \  
&& apt-get clean \  
&& rm google-chrome-stable_current_amd64.deb \  
  
# Font libraries  
&& apt-get -qqy install fonts-ipafont-gothic xfonts-100dpi xfonts-75dpi
xfonts-cyrillic xfonts-scalable libfreetype6 libfontconfig \  
  
# Install Java8 (with use of python-software-properties to do add-apt-
repository)  
&& add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu
xenial main" -y \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get update && apt-get -y install \  
oracle-java8-installer \  
  
# ANDROID  
# System libs for Android enviroment  
&& echo ANDROID_HOME="${ANDROID_HOME}" >> /etc/environment \  
&& dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y \--force-yes expect ant wget libc6-i386 lib32stdc++6
lib32gcc1 lib32ncurses5 lib32z1 qemu-kvm kmod \  
&& apt-get clean \  
&& apt-get autoclean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
# Install Android Tools  
&& mkdir /opt/android-sdk-linux && cd /opt/android-sdk-linux \  
&& wget --output-document=android-tools-sdk.zip --quiet
https://dl.google.com/android/repository/tools_r25.2.3-linux.zip \  
&& unzip -q android-tools-sdk.zip \  
&& rm -f android-tools-sdk.zip \  
&& chown -R root. /opt  
  
# Setup environment  
ENV PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:${GRADLE_HOME}/gradle-${GRADLE_VERSION}/bin  
  
# Install Android SDK  
RUN yes Y | ${ANDROID_HOME}/tools/bin/sdkmanager "build-tools;25.0.2"
"platforms;android-25" "platform-tools"  
RUN cordova telemetry off  
  
WORKDIR Sources  
EXPOSE 8100 35729  
CMD ["ionic", "serve"]  

