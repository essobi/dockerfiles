FROM ubuntu:14.04  
MAINTAINER Sung Park "sunggeun.park@gmail.com"  
RUN apt-get update  
RUN apt-get install -yq curl build-essential libxrender1 libxtst6 libxi6
lib32stdc++6 lib32z1  
  
# Install Node.js  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
# Install Cordova  
RUN npm install -g cordova  
  
# Install Grunt  
RUN npm install -g grunt-cli  
  
# Install Yoeman  
RUN npm install -g yo  
  
# Install Backbone  
RUN npm install generator-mocha  
RUN npm install generator-backbone-mocha  
RUN npm install -g generator-backbone  
  
# Install JDK8  
RUN apt-get install -y ssh software-properties-common  
RUN apt-add-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
RUN apt-get install -yq oracle-java8-installer  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/  
  
# Install Gradle  
RUN apt-get install -yq unzip  
RUN curl -s https://get.sdkman.io | bash  
RUN /bin/bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install
gradle 3.0"  
ENV GRADLE_HOME /root/.sdkman/candidates/gradle/current  
  
# Development user  
RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \  
&& useradd -u 1000 -G sudo -d /home/developer --shell /bin/bash -m developer \  
&& echo "secret\nsecret" | passwd developer  
  
# Install Android Studio  
# Set things up using the dev user and reduce the need for `chown`s  
USER developer  
  
# Android SDK  
RUN curl -sL http://dl.google.com/android/android-sdk_r24.3.3-linux.tgz | tar
-zxv -C /home/developer/  
  
# Android Studio  
RUN cd /opt \  
&& sudo mkdir android-studio \  
&& sudo chown developer:developer android-studio \  
&& curl -L https://dl.google.com/dl/android/studio/ide-zips/1.2.2.0/android-
studio-ide-141.1980579-linux.zip > /tmp/android-studio.zip \  
&& unzip /tmp/android-studio.zip \  
&& rm /tmp/android-studio.zip  
  
ENV ANDROID_HOME="/home/developer/android-sdk-linux" \  
PATH="${PATH}:/home/developer/android-sdk-linux/tools:/home/developer/android-
sdk-linux/platform-tools" \  
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"  
RUN echo y | android update sdk --all --no-ui --force --filter android-22  
RUN echo y | android update sdk --all --no-ui --force --filter platform-tools  
RUN echo y | android update sdk --all --no-ui --force --filter extra-
android-m2repository  
RUN echo y | android update sdk --all --no-ui --force --filter extra-
google-m2repository  
RUN echo y | android update sdk --all --no-ui --force --filter source-22  
RUN echo y | android update sdk --all --no-ui --force --filter build-
tools-22.0.1  
RUN echo y | android update sdk --all --no-ui --force --filter android-21  
RUN echo y | android update sdk --all --no-ui --force --filter build-
tools-21.1.2  
  
RUN sudo ln -s /opt/android-studio/bin/studio.sh /bin/studio  
  
USER root  
  
RUN echo "disable.android.first.run=true" >> /opt/android-
studio/bin/idea.properties  

