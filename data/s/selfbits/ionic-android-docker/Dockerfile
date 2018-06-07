FROM node:8.7  
MAINTAINER Selfbits GmbH <dev@selfbits.io>  
ENV ANDROID_TARGET_SDK="24" \  
ANDROID_BUILD_TOOLS="26.0.2" \  
ANDROID_SDK_TOOLS="24.4.1"  
RUN npm install npm@latest  
RUN rm -rf /usr/local/lib/node_modules/npm  
RUN mv node_modules/npm /usr/local/lib/node_modules/npm  
# Install JDK 8  
RUN echo "deb http://http.debian.net/debian jessie-backports main" | tee
--append /etc/apt/sources.list.d/jessie-backports.list > /dev/null  
RUN apt-get --quiet update --yes  
RUN apt-get --quiet install -t jessie-backports openjdk-8-jdk --yes  
RUN apt-get --quiet install zipalign unzip --yes  
# Set default Java to 8  
RUN update-java-alternatives --set java-1.8.0-openjdk-amd64  
# Install Gradle  
RUN wget -q https://services.gradle.org/distributions/gradle-4.2-bin.zip  
RUN mkdir /opt/gradle  
RUN unzip -d /opt/gradle gradle-4.2-bin.zip  
RUN rm -rf gradle-4.2-bin.zip  
ENV PATH $PATH:/opt/gradle/gradle-4.2/bin  
# Install Android SDK and Build Tools  
RUN wget -q -O android-sdk.tgz https://dl.google.com/android/android-
sdk_r${ANDROID_SDK_TOOLS}-linux.tgz  
RUN tar --extract --gzip --file=android-sdk.tgz  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter android-26  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter android-${ANDROID_TARGET_SDK}  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter platform-tools  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter build-tools-${ANDROID_BUILD_TOOLS}  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter extra-android-m2repository  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter extra-google-google_play_services  
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all
--filter extra-google-m2repository  
RUN rm -rf android-sdk.tgz  
ENV PATH $PATH:$PWD/android-sdk-linux/build-tools/${ANDROID_BUILD_TOOLS}/  
ENV ANDROID_HOME $PWD/android-sdk-linux  
# INSTALL awscli  
RUN apt-get --quiet update --yes  
RUN apt-get --quiet install -y python3  
RUN apt-get install -y python3-pip  
RUN pip3 install awscli  
# INSTALL ionic and cordova  
RUN npm i -g semver @ionic/cli-utils tslib chalk os-name  
RUN npm i -g glob inherits once rimraf @ionic/discover  
RUN npm rebuild node-sass  
RUN npm install -g cordova  
RUN npm i -g ionic@latest && ionic --no-interactive config set -g
daemon.updates false  

