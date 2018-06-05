FROM debian  
  
MAINTAINER Artur Trofymchuk "artur@trofymchuk.net"  
# Install Deps  
RUN apt-get --quiet update --yes  
  
RUN echo deb http://http.debian.net/debian jessie-backports main >>
/etc/apt/sources.list  
  
# install oracle jdk 8  
RUN apt-get update && apt-get --quiet install --yes -f software-properties-
common  
RUN add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu
xenial main"  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 seen
true" | debconf-set-selections  
RUN apt-get update && apt-get --quiet install --yes -f oracle-java8-installer  
  
RUN update-alternatives --config java  
  
RUN apt-get --quiet install --yes wget git unzip lib32stdc++6 lib32z1  
# Install Android SDK  
RUN mkdir /opt/android-sdk-linux  
RUN chown -R root.root /opt/android-sdk-linux  
RUN cd /opt/android-sdk-linux && wget --output-document=android-tools.zip
--quiet https://dl.google.com/android/repository/tools_r25.2.3-linux.zip &&
unzip -q android-tools.zip && rm -f android-tools.zip  
  
# Setup environment  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
RUN mkdir /opt/android-sdk-linux/licenses  
ADD licenses/* /opt/android-sdk-linux/licenses/  
  
# Install sdk elements  
ENV PATH ${PATH}:/opt/android-sdk-linux/tools/bin  
  
RUN echo y | sdkmanager --verbose "platform-tools"  
  
RUN echo y | sdkmanager --verbose "platforms;android-25"  
RUN echo y | sdkmanager --verbose "platforms;android-21"  
  
RUN echo y | sdkmanager --verbose "build-tools;25.0.2"  
  
RUN echo y | sdkmanager --verbose "extras;android;m2repository"  
RUN echo y | sdkmanager --verbose "extras;google;m2repository"  
RUN echo y | sdkmanager --verbose "extras;google;google_play_services"  
RUN echo y | sdkmanager --verbose
"extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2"  
RUN echo y | sdkmanager --verbose "extras;google;google_play_services"  
  
#install gradle  
RUN cd /opt && wget --quiet --output-document=gradle.zip
https://services.gradle.org/distributions/gradle-3.4.1-bin.zip && unzip -q
gradle.zip && rm -f gradle.zip && chown -R root.root /opt/gradle-3.4.1/bin  
ENV PATH ${PATH}:/opt/gradle-3.4.1/bin  
ENV HOME /root  
  
# Set up and run emulator  
#RUN echo y | android --silent update sdk --no-ui --all --filter sys-img-
armeabi-v7a-android-22  
#RUN echo no | android create avd --force -n test -c 30M -t android-22  
#ADD wait-for-emulator /usr/local/bin/  
#ADD start-emulator /usr/local/bin/  
RUN which java  
RUN which android  
RUN which git  
RUN which gradle  
RUN which adb  
  
# Cleaning  
RUN apt-get clean  
  
# GO to workspace  
RUN mkdir -p /opt/workspace  
VOLUME /root/.gradle  
WORKDIR /opt/workspace  

