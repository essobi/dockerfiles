FROM ubuntu:latest  
MAINTAINER Arnold Sergey <upon.the.dark@gmail.com>  
  
RUN apt-get update -qq && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
iptables \  
openssh-server  
  
RUN mkdir -p /var/run/sshd  
  
RUN adduser --quiet jenkins  
RUN echo "jenkins:jenkins" | chpasswd  
RUN mkdir /etc/sudoers.d  
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/jenkins  
  
RUN apt-get install -y --no-install-recommends openjdk-8-jdk  
  
RUN apt-get install -y --no-install-recommends g++-multilib lib32z1
lib32stdc++6  
  
# Downloading android-sdk  
RUN wget http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz; \  
tar zxvf android-sdk_r24.4.1-linux.tgz; \  
mv android-sdk-linux /usr/local/bin/android-sdk ; \  
rm android-sdk_r24.4.1-linux.tgz  
  
#Add env-variables  
ENV ANDROID_HOME /usr/local/bin/android-sdk  
ENV PATH $PATH:$ANDROID_HOME/tools  
ENV PATH $PATH:$ANDROID_HOME/platform-tools  
  
RUN chmod +x $ANDROID_HOME/tools/android  
  
#Update android-libs and other dependencies  
#RUN (sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | android update sdk
--no-ui --filter platform-tools,build-tools-24.0.1,android-24,extra-google-
google_play_services,extra-google-m2repository,extra-android-m2repository  

