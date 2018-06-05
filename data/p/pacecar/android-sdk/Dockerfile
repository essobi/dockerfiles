FROM ruby:2.3  
ARG build_tools_version=26.0.2  
# Installs Oracle JAVA 8  
RUN apt-get update -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu
trusty main' -y && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get remove software-properties-common -y && \  
apt-get autoremove -y && \  
apt-get clean  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Installs Ant  
ENV ANT_VERSION 1.9.7  
RUN cd && \  
wget -q http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \  
mv apache-ant-${ANT_VERSION} /opt/ant && \  
rm apache-ant-${ANT_VERSION}-bin.tar.gz  
ENV ANT_HOME /opt/ant  
ENV PATH ${PATH}:/opt/ant/bin  
  
# Installs i386 architecture required for running 32 bit Android tools  
RUN dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1
openssh-client && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
# Installs Android SDK  
ENV ANDROID_SDK_FILENAME android-sdk_r24.4.1-linux.tgz  
ENV ANDROID_SDK_URL http://dl.google.com/android/${ANDROID_SDK_FILENAME}  
ENV ANDROID_API_LEVELS android-25  
ENV ANDROID_BUILD_TOOLS_VERSION $build_tools_version  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH
${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  
RUN cd /opt && \  
wget -q ${ANDROID_SDK_URL} && \  
tar -xzf ${ANDROID_SDK_FILENAME} && \  
rm ${ANDROID_SDK_FILENAME} && \  
echo y | android update sdk --no-ui -a --filter tools,platform-
tools,${ANDROID_API_LEVELS},build-tools-${ANDROID_BUILD_TOOLS_VERSION},extra-
android-m2repository,extra-google-m2repository,extra-google-
google_play_services,extra-google-play_billing,extra-google-webdriver  
  
# Installs Android NDK  
ENV ANDROID_NDK_HOME /opt/android-ndk  
ENV ANDROID_NDK_VERSION r14b  
ENV PATH ${PATH}:${ANDROID_NDK_HOME}  
RUN apt-get update -y && \  
apt-get install -y cmake unzip && \  
mkdir /opt/android-ndk-tmp && \  
cd /opt/android-ndk-tmp && \  
wget -q https://dl.google.com/android/repository/android-
ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip && \  
unzip -q android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip && \  
mv ./android-ndk-${ANDROID_NDK_VERSION} ${ANDROID_NDK_HOME} && \  
cd && rm -rf /opt/android-ndk-tmp  
  
# Update SDKs to accept licenses - not sure why this is needed  
RUN echo y | sdkmanager --update  
  
# Installs fastlane  
RUN gem install fastlane  

