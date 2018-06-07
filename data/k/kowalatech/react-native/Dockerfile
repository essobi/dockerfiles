FROM phusion/baseimage:0.9.19  
RUN apt-get update && \  
apt-get install software-properties-common \  
python-software-properties \  
wget \  
curl \  
git \  
build-essential \  
lib32gcc1 libc6-i386 lib32z1 lib32stdc++6 \  
apt-transport-https \  
zip \  
unzip -y && \  
apt-get clean  
  
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
  
# Android SDK  
ENV ANDROID_SDK_VERSION r24.4.1  
ENV ANDROID_SDK_FILENAME android-sdk_${ANDROID_SDK_VERSION}-linux.tgz  
ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}  
  
ENV ANDROID_BUILD_TOOLS_VERSION build-tools-26.0.1,build-tools-25.0.3,build-
tools-25.0.2,build-tools-25.0.1,build-tools-25.0.0,build-tools-24.0.1,build-
tools-24,build-tools-23.0.3,build-tools-23.0.2,build-tools-23.0.1  
ENV ANDROID_API_LEVELS android-26,android-25,android-24,android-23  
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
  
# Node and NPM  
ENV NODE_VERSION 8.2.1  
RUN cd && \  
wget -q
http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
&& \  
tar -xzf node-v${NODE_VERSION}-linux-x64.tar.gz && \  
mv node-v${NODE_VERSION}-linux-x64 /opt/node && \  
rm node-v${NODE_VERSION}-linux-x64.tar.gz  
ENV PATH ${PATH}:/opt/node/bin  
RUN npm upgrade  
  
# Apt-get  
RUN apt-get update  
  
# Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install yarn -y  
  
# React tools  
RUN npm install -g react-native-cli  
  
# ImageMagick  
RUN add-apt-repository main  
RUN apt-get install imagemagick -y  
  
ENV LANG en_US.UTF-8  

