FROM ubuntu:17.10  
MAINTAINER contact [at] eliesauveterre [dot] com  
  
ENV DEBIAN_FRONTEND=noninteractive \  
ANDROID_HOME=/opt/android-sdk-linux \  
NODE_VERSION=6.11.2 \  
NPM_VERSION=3.10.10 \  
IONIC_VERSION=3.19.1 \  
BOWER_VERSION=1.7.7 \  
CORDOVA_VERSION=8.0.0 \  
GRUNT_VERSION=0.1.13 \  
GULP_VERSION=3.9.1 \  
SUPPLY_VERSION=2.93.1 \  
ANDROID_SDK_VERSION='3859397' \  
ANDROID_BUILD_TOOLS_VERSION=26.0.2 \  
ANDROID_APIS="android-26"  
# Install basics  
RUN apt-get update && \  
apt-get install -y git wget curl unzip gcc make g++ vim && \  
curl --retry 3 -SLO
"http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz"
&& \  
tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 && \  
rm "node-v$NODE_VERSION-linux-x64.tar.gz" && \  
npm install -g npm@"$NPM_VERSION" && \  
npm install -g grunt-cli@"$GRUNT_VERSION" bower@"$BOWER_VERSION"
cordova@"$CORDOVA_VERSION" ionic@"$IONIC_VERSION" gulp@"$GULP_VERSION" && \  
npm cache clear  
  
# Install Sass  
RUN apt-get install -y ruby-full rubygems ruby-dev libffi-dev  
RUN gem install sass  
  
# Install FireBase  
RUN npm install -g firebase-tools  
  
# Install typings  
RUN npm install -g typings  
  
# ANDROID  
# JAVA  
# install python-software-properties (so you can do add-apt-repository)  
RUN apt-get update && \  
apt-get install -y -q python-software-properties software-properties-common &&
\  
add-apt-repository ppa:webupd8team/java -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update && apt-get -y install oracle-java8-installer  
  
#ANDROID STUFF  
RUN echo ANDROID_HOME="${ANDROID_HOME}" >> /etc/environment && \  
dpkg --add-architecture i386 && \  
apt-get install -y --force-yes expect ant wget gradle libc6-i386 lib32stdc++6
lib32gcc1 lib32ncurses5 lib32z1 qemu-kvm kmod && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Android SDK  
RUN cd /opt && \  
mkdir android-sdk-linux && \  
cd android-sdk-linux && \  
wget https://dl.google.com/android/repository/sdk-tools-
linux-${ANDROID_SDK_VERSION}.zip  
  
RUN cd $ANDROID_HOME && \  
mkdir .android && \  
unzip sdk-tools-linux-${ANDROID_SDK_VERSION}.zip && \  
rm sdk-tools-linux-${ANDROID_SDK_VERSION}.zip  
  
# Setup environment  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:/opt/tools  
RUN echo "export PATH=/opt/android-sdk-linux/build-
tools/${ANDROID_BUILD_TOOLS_VERSION}:/opt/android-sdk-
linux/tools:/opt/android-sdk-linux/platform-tools:/opt/tools:$PATH" >>
/root/.bashrc  
RUN echo "export ANDROID_HOME=/opt/android-sdk-linux" >> /root/.bashrc  
  
# Install sdk elements  
RUN mkdir /root/.android && \  
touch /root/.android/repositories.cfg  
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses  
RUN $ANDROID_HOME/tools/bin/sdkmanager "tools"  
RUN $ANDROID_HOME/tools/bin/sdkmanager "platform-tools"  
RUN $ANDROID_HOME/tools/bin/sdkmanager "build-
tools;${ANDROID_BUILD_TOOLS_VERSION}"  
RUN $ANDROID_HOME/tools/bin/sdkmanager "platforms;${ANDROID_APIS}"  
RUN $ANDROID_HOME/tools/bin/sdkmanager "extras;android;m2repository"  
RUN $ANDROID_HOME/tools/bin/sdkmanager "extras;google;m2repository"  
  
# Install Fastlane Supply for APK publishing  
RUN gem install --no-ri --no-rdoc fastlane -v ${SUPPLY_VERSION}  
  
# Pre download/install the version of gradle used for the installed version of
cordova  
# for faster CI build  
RUN cd /tmp \  
&& export NPM_CONFIG_CACHE=/tmp/.npm \  
&& export NPM_CONFIG_TMP=/tmp/.npm-tmp \  
&& mkdir -p \  
/tmp/.npm \  
/tmp/.npm-tmp \  
&& git config --global user.email "you@example.com" \  
&& git config --global user.name "Your Name" \  
&& echo n | ionic start test-app tabs --no-interactive \  
&& cd test-app \  
&& ionic cordova platform add android --no-interactive \  
&& ionic cordova build android --prod --no-interactive \  
&& rm -rf \  
/root/.android/debug.keystore \  
/root/.config \  
/root/.cordova \  
/root/.ionic \  
/root/.v8flags.*.json \  
/tmp/.npm \  
/tmp/.npm-tmp \  
/tmp/hsperfdata_root/* \  
/tmp/ionic-starter-* \  
/tmp/native-platform*dir \  
/tmp/test-app  
  
# Install Python and AWS tools  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python3.6 get-pip.py  
RUN echo "export PATH=/root/.local/bin:$PATH" >> /root/.bashrc  
RUN export PATH=/root/.local/bin:$PATH  
RUN pip install awsebcli==3.10.1 --upgrade --user  
RUN pip install --upgrade --user awscli  
  
# Install Chrome for Prerender  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' |
tee /etc/apt/sources.list.d/google-chrome.list && \  
apt-get update && \  
apt-get install -y google-chrome-stable  
  
RUN mkdir myApp  
  
### Clean  
RUN apt-get -y autoclean  
RUN apt-get -y clean  
RUN apt-get -y autoremove  
  
VOLUME ["/myApp"]  
  
WORKDIR myApp  
EXPOSE 8100 35729 5037 9222 5554 5555  
CMD ["ionic", "serve"]  

