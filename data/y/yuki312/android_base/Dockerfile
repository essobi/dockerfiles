# Version 1.0.0  
FROM ubuntu:16.04  
MAINTAINER yuki312 <yuki312.m@gmail.com>  
  
# Never ask for confirmations  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-
set-selections  
  
# Install dependent package  
RUN apt-get update && apt-get install -qqy \  
libc6-i386 \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
openjdk-8-jdk \  
software-properties-common \  
unzip \  
wget  
  
# Export JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
# Install apache ant  
RUN cd / && wget -q https://www.apache.org/dist/ant/binaries/apache-
ant-1.9.6-bin.tar.gz  
RUN tar -xvzf apache-ant-1.9.6-bin.tar.gz  
RUN mv apache-ant-1.9.6 /usr/local/  
RUN rm apache-ant-1.9.6-bin.tar.gz  
ENV ANT_HOME /usr/local/apache-ant-1.9.6  
ENV PATH $PATH:$ANT_HOME/bin  
  
# Install gradle  
RUN cd / && wget -q
https://services.gradle.org/distributions/gradle-2.11-all.zip  
RUN unzip gradle-2.11-all.zip  
RUN mv gradle-2.11 /usr/local/  
RUN rm gradle-2.11-all.zip  
ENV GRADLE_HOME /usr/local/gradle-2.11  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Android SDK needs 32bit runtime.  
RUN rm -f /etc/ssl/certs/java/cacerts && /var/lib/dpkg/info/ca-certificates-
java.postinst configure  

