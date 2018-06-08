# Fedora baseline docker container with Oracle JDK and RPM build tools  
# Generated on Sep Aug 12 19:50:51 GMT 2016 using code in this GitHub repo:  
# https://github.com/rigon/docker-fedora-jdk  
# Use the rigon/fedora-rpmtools base image  
FROM rigon/fedora-rpmtools  
MAINTAINER Ricardo Gonçalves <ricardompgoncalves@gmail.com>  
  
ENV JAVA_VERSION 8u121  
ENV BUILD_VERSION b13  
ENV UUID e9e7ea248e2c4826b92b3f075a80e441  
  
# Upgrading system  
RUN dnf -y upgrade  
RUN dnf -y install wget  
  
# Downloading Java  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/$UUID/jdk-$JAVA_VERSION-
linux-x64.rpm" -O /tmp/jdk-8-linux-x64.rpm  
  
RUN dnf -y install /tmp/jdk-8-linux-x64.rpm  
RUN rm /tmp/jdk-8-linux-x64.rpm  
  
RUN alternatives --install /usr/bin/java jar /usr/java/latest/bin/java 200000  
RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws
200000  
RUN alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac
200000  
  
ENV JAVA_HOME /usr/java/latest  
  
# Add JDK bin dir to PATH  
ENV PATH=$PATH:/usr/java/latest/bin/  
  

