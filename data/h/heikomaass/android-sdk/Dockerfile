FROM ubuntu:15.04  
# Inspired from
https://github.com/ksoichiro/dockerfiles/blob/master/android/Dockerfile  
# Inspired from https://github.com/kargs/docker-android/blob/master/Dockerfile  
MAINTAINER heiko.maass@namics.com  
  
RUN dpkg --add-architecture i386  
RUN apt-get update -qq  
RUN apt-get install -y expect  
RUN apt-get install -y --no-install-recommends openjdk-8-jdk  
RUN apt-get install -y --no-install-recommends curl  
RUN apt-get install -y --no-install-recommends libncurses5:i386
libstdc++6:i386 zlib1g:i386  
RUN apt-get install -y --no-install-recommends maven  
  
RUN cd /opt && curl -O http://dl.google.com/android/android-
sdk_r24.4.1-linux.tgz  
RUN cd /opt && tar xzf android-sdk_r24.4.1-linux.tgz  
RUN cd /opt && rm -f android-sdk_r24.4.1-linux.tgz  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
COPY tools /opt/sdk-tools  
ENV PATH ${PATH}:/opt/sdk-tools  
  
RUN ["/opt/sdk-tools/android-accept-licenses.sh", "android update sdk --filter
tools --no-ui --force -a"]  
RUN ["/opt/sdk-tools/android-accept-licenses.sh", "android update sdk --filter
platform-tools --no-ui --force -a"]  
RUN ["/opt/sdk-tools/android-accept-licenses.sh", "android update sdk --filter
\"build-tools-23.0.2\" --no-ui --force -a"]  
RUN ["/opt/sdk-tools/android-accept-licenses.sh", "android update sdk --filter
\"extra-android-support\" --no-ui --force -a"]  
RUN ["/opt/sdk-tools/android-accept-licenses.sh", "android update sdk --filter
\"android-23\" --no-ui --force -a"]  
RUN ["/opt/sdk-tools/android-accept-licenses.sh", "android update sdk --filter
\"extra-android-m2repository\" --no-ui --force -a"]  
RUN ["/opt/sdk-tools/android-accept-licenses.sh", "android update sdk --filter
\"extra-google-m2repository\" --no-ui --force -a"]  
  
RUN apt-get clean  
  
VOLUME /root/.m2  
VOLUME /workspace  
WORKDIR /workspace  

