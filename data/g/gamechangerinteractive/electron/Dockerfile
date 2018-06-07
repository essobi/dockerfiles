FROM ubuntu:xenial  
  
MAINTAINER Nikolay Glushchenko <nick@nickalie.com>  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && apt-get install -y wget curl software-properties-common apt-
transport-https && \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add \- && \  
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' && \  
wget -nc https://dl.winehq.org/wine-builds/Release.key && \  
apt-key add Release.key && \  
rm Release.key && \  
apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/ && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \- &&
\  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y \--no-install-recommends winehq-stable build-essential
nodejs git-core ssh default-jdk unzip google-cloud-sdk imagemagick yarn
google-chrome-stable && \  
wget -O libpng12-0.deb
http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb
&& \  
dpkg -i libpng12-0.deb && \  
rm libpng12-0.deb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV CHROME_BIN /usr/bin/google-chrome  
  
RUN wineboot && wineboot -s  
  
# Install Android SDK  
ENV ANDROID_HOME /opt/android-sdk  
  
RUN mkdir -p $ANDROID_HOME && \  
cd $ANDROID_HOME && \  
wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip -O
tools.zip && \  
unzip tools.zip && \  
rm -f tools.zip && \  
mkdir $ANDROID_HOME/licenses && \  
echo 8933bad161af4178b1185d1a37fbf41ea5269c55 >
$ANDROID_HOME/licenses/android-sdk-license && \  
echo d56f5187479451eabf01fb78af6dfcb131a6481e >>
$ANDROID_HOME/licenses/android-sdk-license && \  
echo 84831b9409646a918e30573bab4c9c91346d8abd >
$ANDROID_HOME/licenses/android-sdk-preview-license  
  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
RUN sdkmanager --verbose "build-tools;27.0.3"  
  
# Install Gradle  
ENV GRADLE_HOME /opt/gradle  
ENV GRADLE_VERSION 4.6  
  
RUN wget -O gradle.zip
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"
&& \  
unzip gradle.zip && \  
rm gradle.zip && \  
mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" && \  
ln \--symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle  
  
# preloading cordova 8 dependencies  
RUN yarn global add cordova && \  
cordova create hello com.example.hello HelloWorld && \  
cd hello && \  
cordova platform add \--save android && \  
cordova plugin add \--save cordova-plugin-splashscreen && \  
cordova plugin add \--save cordova-plugin-fullscreen && \  
cordova build && \  
cd .. && rm -rf hello && \  
yarn global remove cordova  
  
# preloading cordova 7 dependencies  
RUN yarn global add cordova@7.1.0 && \  
cordova create hello com.example.hello HelloWorld && \  
cd hello && \  
cordova platform add \--save android@6.2.3 && \  
cordova plugin add \--save cordova-plugin-splashscreen && \  
cordova plugin add \--save cordova-plugin-fullscreen && \  
cordova build && \  
cd .. && rm -rf hello && \  
yarn global remove cordova  
  
RUN wget
https://github.com/netlify/netlifyctl/releases/download/v0.3.3/netlifyctl-
linux-amd64-0.3.3.tar.gz && \  
tar -xzf netlifyctl-linux-amd64-0.3.3.tar.gz && \  
rm -rf netlifyctl-linux-amd64-0.3.3.tar.gz && \  
mv netlifyctl /usr/bin/netlifyctl

