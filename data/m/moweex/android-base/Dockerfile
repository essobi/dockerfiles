# Pull base image.  
FROM ubuntu:14.04  
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
#ENV ANDROID_SDK_VERSION r24.4.1  
#ENV ANDROID_BUILD_TOOLS_VERSION build-tools-23.0.1,build-tools-23.0.3,build-
tools-25.0.0,build-tools-25.0.2,build-tools-25.0.3,build-tools-26.0.1  
#ENV ANDROID_SDK_FILENAME android-sdk_${ANDROID_SDK_VERSION}-linux.tgz  
#ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}  
#ENV ANDROID_API_LEVELS android-23,android-25,android-26  
#ENV ANDROID_EXTRA_COMPONENTS extra-android-m2repository,extra-
google-m2repository  
#ENV ANDROID_HOME /opt/android-sdk-linux  
#ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
#RUN cd /opt && \  
# wget -q ${ANDROID_SDK_URL} && \  
# tar -xzf ${ANDROID_SDK_FILENAME} && \  
# rm ${ANDROID_SDK_FILENAME} && \  
# echo y | android update sdk --no-ui -a --filter tools,platform-
tools,${ANDROID_API_LEVELS},${ANDROID_BUILD_TOOLS_VERSION} && \  
# echo y | android update sdk --no-ui --all --filter
"${ANDROID_EXTRA_COMPONENTS}"  
ENV SDK_URL="https://dl.google.com/android/repository/sdk-tools-
linux-3859397.zip" \  
ANDROID_HOME="/usr/local/android-sdk" \  
ANDROID_VERSION=26 \  
ANDROID_BUILD_TOOLS_VERSION=26.0.2  
# Download Android SDK  
RUN mkdir "$ANDROID_HOME" .android \  
&& cd "$ANDROID_HOME" \  
&& curl -o sdk.zip $SDK_URL \  
&& unzip sdk.zip \  
&& rm sdk.zip \  
&& yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses  
  
# Install Android Build Tool and Libraries  
RUN $ANDROID_HOME/tools/bin/sdkmanager --update  
RUN $ANDROID_HOME/tools/bin/sdkmanager "build-
tools;${ANDROID_BUILD_TOOLS_VERSION}" \  
"platforms;android-${ANDROID_VERSION}" \  
"platforms;android-25" \  
"platforms;android-23" \  
"platform-tools"  
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

