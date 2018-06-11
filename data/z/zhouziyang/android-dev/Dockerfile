FROM ubuntu:14.04  
MAINTAINER Ziyang Zhou <ziyang.zhou1987@gmail.com>  
  
RUN apt-get -qq update  
RUN apt-get -qqy install wget ant  
  
RUN wget -nv --no-check-certificate --no-cookies \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie"\  
-O /opt/jdk.tgz \  
http://download.oracle.com/otn-pub/java/jdk/8u5-b13/jdk-8u5-linux-x64.tar.gz  
RUN cd /opt && tar xfz /opt/jdk.tgz  
RUN rm /opt/jdk.tgz  
ENV JAVA_HOME /opt/jdk1.8.0_05  
ENV PATH $PATH:$JAVA_HOME/bin  
  
RUN wget -nv -O /opt/android-sdk.tgz \  
"http://dl.google.com/android/android-sdk_r22.6.2-linux.tgz"  
RUN cd /opt && tar xfz /opt/android-sdk.tgz  
RUN rm /opt/android-sdk.tgz  
ENV ANDROID_HOME /opt/android-sdk-linux  
  
RUN chmod 555 $ANDROID_HOME/tools/android  
RUN echo "Y" | $ANDROID_HOME/tools/android update sdk --no-ui \  
\--filter tools,platform-tools,build-tools-19.1.0,android-19  
  
RUN wget -nv -O /opt/android-ndk.tar.bz2 \  
"http://dl.google.com/android/ndk/android-ndk-r9d-linux-x86_64.tar.bz2"  
RUN cd /opt && tar xjf /opt/android-ndk.tar.bz2  
RUN rm /opt/android-ndk.tar.bz2  
ENV ANDROID_NDK_HOME /opt/android-ndk-r9d  

