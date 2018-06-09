# Pull base image.  
FROM ubuntu:latest  
  
# Install base software packages  
RUN apt-get update && \  
apt-get install software-properties-common \  
python-software-properties \  
wget \  
curl \  
git \  
unzip -y && \  
apt-get clean  
  
# ——————————  
# Install Java.  
# ——————————  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
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
ENV GRADLE_VERSION 2.4  
RUN cd /usr/lib \  
&& curl -fl
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
gradle-bin.zip \  
&& unzip "gradle-bin.zip" \  
&& ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \  
&& rm "gradle-bin.zip"  
  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME /usr/lib/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
  
# ——————————  
# Install Node and global packages  
# ——————————  
ENV NODE_VERSION 6.11.1  
RUN cd && \  
wget -q
http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
&& \  
tar -xzf node-v${NODE_VERSION}-linux-x64.tar.gz && \  
mv node-v${NODE_VERSION}-linux-x64 /opt/node && \  
rm node-v${NODE_VERSION}-linux-x64.tar.gz  
ENV PATH ${PATH}:/opt/node/bin  
  
  
# ——————————  
# Install Yarn  
# ——————————  
ENV YARN_VERSION 0.27.5  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
# ——————————  
# Install Basic React-Native packages  
# ——————————  
RUN yarn global add react-native-cli  
  
ENV LANG en_US.UTF-8  

