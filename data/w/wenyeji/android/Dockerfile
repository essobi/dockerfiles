FROM java:8-jdk  
  
MAINTAINER wenyeji "wenyeji@gmail.com"  
ENV ANT_VERSION 1.9.7  
RUN cd && \  
wget -q http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \  
mv apache-ant-${ANT_VERSION} /opt/ant && \  
rm apache-ant-${ANT_VERSION}-bin.tar.gz  
ENV ANT_HOME /opt/ant  
ENV PATH ${PATH}:/opt/ant/bin  
  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
--force-yes expect git wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5
lib32z1 python curl  
  
ENV ANDROID_VERSION r24.4.1  
RUN cd /opt && wget -O android-sdk.tgz -q
http://dl.google.com/android/android-sdk_${ANDROID_VERSION}-linux.tgz && tar
xzf android-sdk.tgz && rm -f android-sdk.tgz && chown -R root.root android-
sdk-linux  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
  
COPY tools /opt/tools  
ENV PATH ${PATH}:/opt/tools  
RUN ["/opt/tools/android-accept-licenses.sh", "android update sdk --all
--force --no-ui --filter platform-tools,tools,build-
tools-15.1.0,android-15,extra-android-support,extra-android-m2repository"]  
  
RUN apt-get clean  
RUN echo "Asia/Shanghai" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  

