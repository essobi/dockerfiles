FROM java:8  
MAINTAINER Renato Ivancic <renato.ivancic@gmail.com>  
  
ENV ANDROID_VERSION android-24  
ENV ANDROID_SDK_VERSION 24.4.1  
ENV BUILD_TOOLS_VERSION build-tools-24.0.3  
ENV GRADLE_VERSION 2.14.1  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV GRADLE_USER_HOME /usr/bin/gradle  
  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV PATH $PATH:$ANDROID_HOME/tools:$GRADLE_USER_HOME/bin  
  
# install 32-bit dependencies  
RUN apt-get update -y && \  
dpkg --add-architecture i386 && \  
apt-get update -y && \  
apt-get install -y libncurses5:i386 libstdc++6:i386 zlib1g:i386  
  
# install Gradle  
ADD https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip
/usr/bin/gradle.zip  
WORKDIR /usr/bin  
RUN apt-get install -y unzip && \  
unzip gradle.zip && \  
ln -s gradle-${GRADLE_VERSION} gradle && \  
rm gradle.zip && \  
apt-get remove -y unzip  
  
# install android SDK  
ADD http://dl.google.com/android/android-sdk_r${ANDROID_SDK_VERSION}-linux.tgz
/tmp/android-sdk-linux.tgz  
RUN mkdir -p $ANDROID_HOME && \  
tar -xzf /tmp/android-sdk-linux.tgz -C /tmp && \  
mv /tmp/android-sdk-linux/* $ANDROID_HOME && \  
( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | android update sdk
--no-ui --all --filter platform-
tools,${ANDROID_VERSION},${BUILD_TOOLS_VERSION},extra-
android-m2repository,extra-android-support,extra-google-
google_play_services,extra-google-m2repository  
# clean up  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
VOLUME /build  
  
WORKDIR /build  
  
CMD ["gradle", "-version"]  

