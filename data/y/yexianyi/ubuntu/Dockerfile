# This is a comment  
FROM ubuntu:16.04  
  
ARG JDK_VERSION=jdk-8u101  
ARG JDK_PACKAGE=$JDK_VERSION-linux-x64.tar.gz  
ARG JDK_INSTALL_PATH=/usr/lib/java  
  
ENV JAVA_HOME=$JDK_INSTALL_PATH/jdk1.8.0_101  
ENV PATH=$JAVA_HOME/bin:$HBASE_HOME/bin:$PATH  
  
  
MAINTAINER Xianyi Ye <https://cn.linkedin.com/in/yexianyi>  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& apt-get clean \  
&& apt-get autoremove \  
  
# Install Oracle JDK  
&& mkdir /usr/lib/java \  
&& cd /usr/lib/java \  
&& wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u101-b13/$JDK_PACKAGE \  
&& tar -xzvf $JDK_PACKAGE \  
&& rm ./$JDK_PACKAGE \

