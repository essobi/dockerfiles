FROM datencia/ionic  
  
LABEL maintainer="david.atencia@gmail.com"  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle \  
ANDROID_HOME=/opt/android-sdk-linux \  
GRADLE_HOME=/opt/gradle \  
GRADLE_VERSION=4.5.1  
  
RUN echo "Installing build dependencies" && \  
apt-get -qq update && \  
apt-get -qq install -y wget unzip software-properties-common --no-install-
recommends && \  
echo "Installing Java JDK 8" && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get -qq update -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get -qq install -y oracle-java8-installer oracle-java8-set-default && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
echo "Installing Gradle" && \  
wget -O gradle.zip -nv
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip &&
\  
unzip -q gradle.zip && \  
rm -f gradle.zip && \  
mv gradle-${GRADLE_VERSION} ${GRADLE_HOME} && \  
chown -R root:root ${GRADLE_HOME} && \  
echo "Installing Android SDK" && \  
dpkg --add-architecture i386 && \  
apt-get -qq update && \  
apt-get -qq install -y lib32ncurses5 lib32stdc++6 && \  
mkdir ${ANDROID_HOME} && cd ${ANDROID_HOME} && \  
wget -O android-tools-sdk.zip -nv
https://dl.google.com/android/repository/tools_r25.2.5-linux.zip && \  
unzip -q android-tools-sdk.zip && \  
rm -f android-tools-sdk.zip && \  
yes Y | ${ANDROID_HOME}/tools/bin/sdkmanager "build-tools;27.0.3"
"platforms;android-23" "platforms;android-24" "platforms;android-25"
"platforms;android-26" "platform-tools" "extras;android;m2repository" && \  
chown -R root:root ${ANDROID_HOME} && \  
echo "Cleaning up" && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get purge -y \--auto-remove software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean  
  
ENV PATH
$PATH:${GRADLE_HOME}/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools  

