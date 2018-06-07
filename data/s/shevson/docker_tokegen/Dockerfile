FROM ubuntu:14.04  
MAINTAINER michmatusz  
  
#Overall update  
RUN apt-get update -qq  
  
# Java & libs  
RUN apt-get install -y software-properties-common && add-apt-repository -y
ppa:webupd8team/java && apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
--force-yes expect git wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5
lib32z1  
  
# Android SDK  
RUN apt-get install -y --no-install-recommends wget  
RUN cd /opt && wget -q http://dl.google.com/android/android-
sdk_r24.3.4-linux.tgz  
RUN cd /opt && tar xzf android-sdk_r24.3.4-linux.tgz  
RUN cd /opt && rm -f android-sdk_r24.3.4-linux.tgz  
  
#Setting up android_home  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
#Update sdk  
RUN echo y | android update sdk --all --no-ui --filter platform-tools,build-
tools-22.0.1,android-22,extra-android-m2repository,extra-
google-m2repository,extra-android-support,extra-google-google_play_services  
  
#Scripts  
ADD start-container.sh /usr/local/bin/start-container.sh  
RUN chmod +x /usr/local/bin/start-container.sh  
  
#Clean  
RUN apt-get clean  
  
# End  
RUN mkdir -p /opt/workspace  
CMD ["/usr/local/bin/start-container.sh"]  
WORKDIR /opt/workspace

