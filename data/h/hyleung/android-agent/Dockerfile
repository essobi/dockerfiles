FROM hyleung/jenkins-agent  
MAINTAINER H.Y. Leung <hy.leung@gmail.com>  
  
#Install curl  
RUN apt-get install -y curl  
  
#Download the Android sdk into a temp directory  
RUN mkdir ~/temp  
RUN curl http://dl.google.com/android/android-sdk_r23.0.2-linux.tgz -o
~/temp/android-sdk.tgz  
  
#Android is compile for 32-bit systems, install the 32-bit versions of
dependencies  
# http://askubuntu.com/questions/147400/problems-with-eclipse-and-android-sdk  
RUN apt-get -y install lib32z1 lib32ncurses5 lib32bz2-1.0 lib32stdc++6  
  
#Unzip  
RUN tar zvxf ~/temp/android-sdk.tgz -C /usr/local  
RUN chown -R root:root /usr/local/android-sdk-linux  
RUN chmod g+w -R /usr/local/android-sdk-linux  
  
#Install the SDK tools  
ENV ANDROID_HOME /usr/local/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--filter platform-tools,build-tools  
#Build tools 19.1.0  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui -a
--filter build-tools-19.1.0  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui -a
--filter build-tools-20.0.0  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--filter android-20,android-19,android-18,android-17,android-16  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--filter extra-android-support  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--filter extra-android-m2repository  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--filter extra-google-m2repository  
RUN echo y | /usr/local/android-sdk-linux/tools/android update sdk --no-ui
--filter extra-google-google_play_services  
  
RUN chmod -R 777 /tmp/  
  

