#base image  
FROM ubuntu  
  
MAINTAINER Alexey Kuznetsov <kuznetsovalexey34@gmail.com>  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN echo "export DEBIAN_FRONTEND=noninteractive" >> /etc/environment  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
RUN echo "export ANDROID_HOME=/opt/android-sdk-linux" >> /etc/environment  
  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:/opt/gradle/gradle-4.4.1/bin  
  
RUN echo "export
PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-
tools:/opt/gradle/gradle-4.4.1/bin" >> /etc/environment  
  
RUN echo "root:root" | chpasswd  
  
RUN useradd -ms /bin/bash jenkins  
  
RUN echo "jenkins:jenkins" | chpasswd  
  
#install java  
RUN apt-get update && apt-get -y upgrade && apt-get install -y software-
properties-common && apt-add-repository -y ppa:webupd8team/java && apt-get
update && echo debconf shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && echo debconf shared/accepted-oracle-license-v1-1
seen true | debconf-set-selections && apt-get install -y oracle-
java8-installer  
  
#Install Deps  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
expect git wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 python
curl unzip  
  
#Install a basic SSH server  
RUN apt-get install -y openssh-server  
  
RUN mkdir -p /var/run/sshd  
  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
#SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
#Install Android SDK  
RUN mkdir /opt/android-sdk-linux && cd /opt/android-sdk-linux && wget
https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && unzip
sdk-tools-linux-3859397.zip && rm -f sdk-tools-linux-3859397.zip  
  
RUN chown -R root:jenkins /opt/android-sdk-linux && chmod -R 775 /opt/android-
sdk-linux  
  
#install ant  
RUN apt-get install -y ant  
  
#install vim  
RUN apt-get install -y vim  
  
#install deps for build-specific tools  
RUN yes | /opt/android-sdk-linux/tools/bin/sdkmanager --licenses  
  
USER jenkins  
  
RUN mkdir -p ~/.android && touch ~/.android/repositories.cfg  
  
USER root  
  
RUN yes | /opt/android-sdk-linux/tools/bin/sdkmanager "ndk-bundle"
"platforms;android-23" "build-tools;23.0.2" "build-tools;23.0.3"
"extras;android;m2repository"  
  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* && localedef -i en_US -c -f UTF-8 -A
/usr/share/locale/locale.alias en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
RUN echo "export LANG=en_US.UTF-8" >> /etc/environment  
  
#Cleaning  
RUN apt-get clean  
  
RUN apt-get autoclean  
  
RUN apt-get autoremove  
  
#Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  

