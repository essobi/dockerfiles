# Pull base image.  
FROM ubuntu:14.04  
# Install base software packages  
RUN apt-get update && \  
apt-get install software-properties-common \  
python-software-properties \  
wget \  
curl \  
git \  
unzip -y --no-install-recommends && \  
apt-get clean  
  
# ——————————  
# Install Java.  
# ——————————  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer --no-install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
  
# ——————————  
# Installs i386 architecture required for running 32 bit Android tools  
# ——————————  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
# ——————————  
# Installs Android SDK  
# ——————————  
ENV ANDROID_SDK_VERSION r24.4.1  
ENV ANDROID_BUILD_TOOLS_VERSION build-tools-23.0.3,build-tools-23.0.2,build-
tools-23.0.1  
ENV ANDROID_SDK_FILENAME android-sdk_${ANDROID_SDK_VERSION}-linux.tgz  
ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}  
ENV ANDROID_API_LEVELS android-23  
ENV ANDROID_EXTRA_COMPONENTS extra-android-m2repository,extra-
google-m2repository  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
RUN cd /opt && \  
wget -q ${ANDROID_SDK_URL} && \  
tar -xzf ${ANDROID_SDK_FILENAME} && \  
rm ${ANDROID_SDK_FILENAME} && \  
echo y | android update sdk --no-ui -a --filter tools,platform-
tools,${ANDROID_API_LEVELS},${ANDROID_BUILD_TOOLS_VERSION} && \  
echo y | android update sdk --no-ui --all --filter
"${ANDROID_EXTRA_COMPONENTS}"  
  
# ——————————  
# Installs Gradle  
# ——————————  
# Gradle  
ENV GRADLE_VERSION 3.1  
RUN cd /usr/lib \  
&& curl -fl
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
gradle-bin.zip \  
&& unzip "gradle-bin.zip" \  
&& ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle  
# && rm "gradle-bin.zip"  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME /usr/lib/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
  
# ——————————  
# Install Node and global packages  
# ——————————  
ENV NODE_VERSION 6.9.1  
RUN cd && \  
wget -q
http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
&& \  
tar -xzf node-v${NODE_VERSION}-linux-x64.tar.gz && \  
mv node-v${NODE_VERSION}-linux-x64 /opt/node && \  
rm node-v${NODE_VERSION}-linux-x64.tar.gz  
ENV PATH ${PATH}:/opt/node/bin  
  
  
# ——————————  
# Install React-Native packages  
# ——————————  
RUN mkdir -p /opt/yarn && \  
cd /opt/yarn && \  
wget -q https://yarnpkg.com/latest.tar.gz && \  
tar -xzf latest.tar.gz --strip 1  
ENV PATH "$PATH:/opt/yarn/bin"  
# Yarn is now in /opt/yarn/  
RUN mkdir -p /workdir && \  
cd /workdir  
RUN yarn global add react-native-cli \  
yarn global add gulp  
#RUN echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf &&
sudo sysctl -p  
RUN sysctl -w fs.inotify.max_user_watches=1048576  
  
#RUN npm install react-native-cli -g  
#RUN npm install rnpm -g  
#RUN mkdir workdir \  
# cd workdir \  
# npm install create-react-app -g \  
# create-react-app eod \  
# cd eod  
ENV LANG en_US.UTF-8  

