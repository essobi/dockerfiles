FROM phusion/baseimage  
MAINTAINER James Baxter <j.w.baxter@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -q && apt-get install wget -qqy  
  
ENV JDK_VERSION 8u111  
ENV JDK_BUILD 14  
ENV JDK_FOLDER jdk1.8.0_111  
  
RUN wget -q --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/${JDK_VERSION}-b${JDK_BUILD}/jdk-${JDK_VERSION}-linux-x64.tar.gz  
RUN mkdir /usr/lib/jvm && \  
tar -C /usr/lib/jvm -zxf jdk-${JDK_VERSION}-linux-x64.tar.gz && \  
ln -s /usr/lib/jvm/${JDK_FOLDER} /usr/lib/jvm/jdk && \  
update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk/bin/javac
1 && \  
update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk/bin/java 1
&& \  
update-alternatives --set javac /usr/lib/jvm/jdk/bin/javac && \  
update-alternatives --set java /usr/lib/jvm/jdk/bin/java && \  
export JAVA_HOME=/usr/lib/jvm/jdk && \  
export PATH=$PATH:$JAVA_HOME/bin  

