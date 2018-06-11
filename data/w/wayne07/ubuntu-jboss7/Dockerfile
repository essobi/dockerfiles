FROM ubuntu:15.04  
MAINTAINER Jürgen Seliger <juergen.seliger@gmail.com>  
  
RUN apt-get update && apt-get -y install wget curl unzip  
  
ENV JDK_VERSION 7u75  
ENV JDK_BUILD b13  
ENV JAVA_FILE jdk-$JDK_VERSION-linux-x64.tar.gz  
  
WORKDIR /opt/java  
  
RUN cd /tmp && \  
wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/$JDK_VERSION-$JDK_BUILD/$JAVA_FILE && \  
wget http://download.jboss.org/jbossas/7.1/jboss-as-7.1.1.Final/jboss-
as-7.1.1.Final.zip && \  
tar -xzvf $JAVA_FILE && \  
unzip jboss-as-7.1.1.Final.zip && \  
rm -f /tmp/$JAVA_FILE && \  
rm -f /tmp/jboss-as-7.1.1.Final.zip && \  
mv /tmp/jdk1.7.0_75 /opt/java && \  
mv /tmp/jboss-as-7.1.1.Final /opt  

