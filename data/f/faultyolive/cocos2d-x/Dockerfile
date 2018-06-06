FROM ubuntu:14.04.3  
MAINTAINER Nelson Silva <nelson.silva@faultyolive.com>  
  
# Build-Variables  
ENV ANDROID_SDK_VERSION r23.0.2  
ENV ANDROID_NDK_VERSION r10e  
ENV ANDROID_BUILD_TOOLS_VERSION 22.0.1  
ENV ANDROID_APIS android-16  
ENV COCOS2D_X_VERSION 3.8.1  
# Set Environment Variables  
ENV ANT_HOME /usr/share/ant  
ENV MAVEN_HOME /usr/share/maven  
ENV GRADLE_HOME /usr/share/gradle  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV ANDROID_SDK_ROOT $ANDROID_HOME  
ENV NDK_HOME /opt/android-ndk-$ANDROID_NDK_VERSION  
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-
tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION  
ENV PATH $PATH:$ANT_HOME/bin  
ENV PATH $PATH:$MAVEN_HOME/bin  
ENV PATH $PATH:$GRADLE_HOME/bin  
ENV PATH $PATH:$NDK_HOME  
ENV PATH $PATH:/opt/cocos2d-x-$COCOS2D_X_VERSION/tools/cocos2d-console/bin  
  
WORKDIR "/opt"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install 386 arch packages required by the android sdk  
RUN dpkg --add-architecture i386 && \  
apt-get update -qq && \  
apt-get dist-upgrade -y --no-install-recommends  
RUN apt-get install -y libncurses5:i386 libstdc++6:i386 zlib1g:i386  
  
# Install development packages  
RUN apt-get install -y wget curl unzip git build-essential make python  
  
# Set WebUpd8 PPA  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
&& \  
apt-get update -y  
  
# Install java8 and automatically accept the Oracle license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
RUN apt-get install -y oracle-java8-set-default  
  
# Install Ant  
RUN apt-get install -y ant  
  
# Install Gradle 2.5  
RUN wget https://services.gradle.org/distributions/gradle-2.5-bin.zip -P /tmp
&& \  
unzip /tmp/gradle-2.5-bin.zip -d /usr/share/ && \  
ln -s /usr/share/gradle-2.5 /usr/share/gradle  
  
# Install Android SDK  
RUN curl -L http://dl.google.com/android/android-sdk_$ANDROID_SDK_VERSION-
linux.tgz | \  
tar -xz -C .  
RUN echo y | android update sdk -a -u -t platform-tools,${ANDROID_APIS},build-
tools-${ANDROID_BUILD_TOOLS_VERSION}  
  
# Install Android NDK  
RUN wget http://dl.google.com/android/ndk/android-
ndk-${ANDROID_NDK_VERSION}-linux-x86.bin && \  
chmod u+x android-ndk-${ANDROID_NDK_VERSION}-linux-x86.bin && \  
./android-ndk-${ANDROID_NDK_VERSION}-linux-x86.bin -y && \  
rm android-ndk-${ANDROID_NDK_VERSION}-linux-x86.bin  
  
# Install cocos2d-x  
RUN wget http://cocos2d-x.org/filedown/cocos2d-x-$COCOS2D_X_VERSION.zip && \  
unzip cocos2d-x-$COCOS2D_X_VERSION.zip && \  
rm cocos2d-x-$COCOS2D_X_VERSION.zip && \  
cd cocos2d-x-$COCOS2D_X_VERSION && \  
python setup.py  
  
# Clean up  
RUN apt-get autoremove -y  
RUN apt-get clean  

