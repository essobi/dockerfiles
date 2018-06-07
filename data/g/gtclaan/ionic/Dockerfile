FROM node:7.2.0  
# Install npm packages  
COPY bower.json /  
RUN npm config -g set strict-ssl false && git config --global
url."https://".insteadOf git:// && echo '{"strict-
ssl":false,"registry":"https://bower.herokuapp.com"}' > ~/.bowerrc && npm
install -g bower && bower install --allow-root && npm install -g cordova@6.4.0
&& npm install -g ionic@1.7.16 && npm install -g gulp-cli && npm install -g
gulp  
  
# Prepare install Oracle JDK 8  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && echo "deb-src
http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a
/etc/apt/sources.list.d/webupd8team-java.list && apt-key adv --keyserver
hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && echo oracle-
java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
  
# Update apt sources  
RUN apt-get update  
  
# Install Oracle JDK 8  
RUN apt-get install -y oracle-java8-installer  
  
# Install additional packages from apt  
RUN apt-get install -y unzip apt-transport-https  
  
# Android SDK Tools installation  
RUN mkdir /opt/android && wget
https://dl.google.com/android/repository/tools_r25.2.5-linux.zip -O
/opt/android/android-sdk-tools.zip && unzip /opt/android/android-sdk-tools.zip
-d /opt/android && rm /opt/android/android-sdk-tools.zip && echo 'export
ANDROID_HOME=/opt/android' >> ~/.bashrc && echo 'export
PATH=$PATH:$ANDROID_HOME/tools' >> ~/.bashrc && echo 'export
PATH=$PATH:$ANDROID_HOME/platform-tools' >> ~/.bashrc  
  
# Install  
# - Android SDK Platform-tools (latest)  
# - Android SDK Build-tools (latest)  
# - SDK Platform Android 7.0, API 24 (latest)  
RUN . ~/.bashrc && PACKAGES="$(android list sdk | grep -E '(SDK Platform-
tools|SDK Build-tools|SDK Platform Android 7.0, API 24)' | sed
's/\\([0-9]\\).*/\1/' | tr '\n' ',' | tr -d ' ')" && printf "yes\n" | android
update sdk --no-ui --filter $PACKAGES

