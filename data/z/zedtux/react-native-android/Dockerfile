FROM aptible/ruby:2.4-ubuntu-16.04  
# —————————————  
# Install java8  
# —————————————  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
(echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections) && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean && \  
rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# ————————————  
# Install Deps  
# ————————————  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y curl \  
git \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
libc6-i386 \  
libcurl4-openssl-dev \  
libpulse0 \  
libqt5widgets5 \  
python \  
unzip && \  
apt-get clean && \  
rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
RUN mkdir ${ANDROID_HOME}  
  
# ———————————————————  
# Install Android SDK  
# ———————————————————  
ENV ANDROID_SDK_URL "https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip"  
RUN cd ${ANDROID_HOME} && \  
curl -L ${ANDROID_SDK_URL} -o android-sdk-tools.zip && \  
unzip -q android-sdk-tools.zip && \  
rm -f android-sdk-tools.zip  
  
ENV ANDROID_VERSION 26  
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses && \  
yes | ${ANDROID_HOME}/tools/bin/sdkmanager --verbose \  
'tools' \  
'platform-tools' \  
'emulator' \  
'build-tools;26.0.3' \  
"platforms;android-${ANDROID_VERSION}" \  
'extras;android;m2repository' \  
'extras;google;m2repository' \  
'extras;google;google_play_services' \  
"system-images;android-${ANDROID_VERSION};google_apis;x86"  
  
# Use correct Qt libs for emulator  
ENV LD_LIBRARY_PATH ${ANDROID_HOME}/emulator/lib64/qt/lib/  
  
# —————————————————  
# Setup environment  
# —————————————————  
ENV PATH
${PATH}:${ANDROID_HOME}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
  
# ————————————————————————————————  
# Install Node and global packages  
# ————————————————————————————————  
ENV NODE_VERSION 8.11.2  
RUN cd && \  
curl -L
http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
-o node-v${NODE_VERSION}-linux-x64.tar.gz && \  
tar -xzf node-v${NODE_VERSION}-linux-x64.tar.gz && \  
mv node-v${NODE_VERSION}-linux-x64 /opt/node && \  
rm node-v${NODE_VERSION}-linux-x64.tar.gz  
ENV PATH ${PATH}:/opt/node/bin  
  
# ————————————  
# Install Yarn  
# ————————————  
ENV YARN_VERSION 1.7.0  
RUN cd && \  
curl -L
https://github.com/yarnpkg/yarn/releases/download/v${YARN_VERSION}/yarn_${YARN_VERSION}_all.deb
-o yarn_${YARN_VERSION}_all.deb && \  
dpkg -i ./yarn_${YARN_VERSION}_all.deb && \  
rm yarn_${YARN_VERSION}_all.deb  
  
ENV LANG en_US.UTF-8  
# Imports tools  
COPY tools/ /usr/local/bin  
RUN chmod +x /usr/local/bin/*  

