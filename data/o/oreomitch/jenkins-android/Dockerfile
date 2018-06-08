#######################################################################  
# Dockerfile to build Crate.io container image  
# Based on Ubuntu  
#######################################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:12.04  
  
# File Author / Maintainer  
MAINTAINER Mitchell Wong Ho <oreomitch@gmail.com>  
  
# RUN echo "deb http://archive.ubuntu.com/ubuntu precise universe" >>
/etc/apt/sources.list  
RUN apt-get update  
  
# Never ask for confirmations  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" |
/usr/bin/debconf-set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" |
/usr/bin/debconf-set-selections  
  
# Add oracle-jdk6 to repositories  
RUN apt-get update  
RUN apt-get install python-software-properties -y  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get install oracle-java6-installer -y  
RUN apt-get install oracle-java6-set-default -y  
  
ENV JAVA_HOME /usr/bin/java  
ENV PATH $JAVA_HOME:$PATH  
  
# Add Android SDK  
RUN wget --progress=dot:giga http://dl.google.com/android/android-
sdk_r22.6.2-linux.tgz  
RUN mv android-sdk_r22.6.2-linux.tgz /opt/  
RUN cd /opt && tar xzvf ./android-sdk_r22.6.2-linux.tgz  
ENV ANDROID_HOME /opt/android-sdk-linux/  
ENV PATH $ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH  
RUN echo $PATH  
RUN echo "y" | android update sdk -u --filter platform-tools,android-19,build-
tools-19.0.3  
RUN chmod -R 755 $ANDROID_HOME  
  
RUN apt-get install -y unzip  
ADD https://services.gradle.org/distributions/gradle-0.9-bin.zip /opt/  
RUN unzip /opt/gradle-0.9-bin.zip -d /opt  
ENV GRADLE_HOME /opt/gradle-0.9  
ENV PATH $GRADLE_HOME/bin:$PATH  
  
# Fake a fuse install (to prevent ia32-libs-multiarch package from producing
errors)  
RUN apt-get install libfuse2  
RUN cd /tmp ; apt-get download fuse  
RUN cd /tmp ; dpkg-deb -x fuse_* .  
RUN cd /tmp ; dpkg-deb -e fuse_*  
RUN cd /tmp ; rm fuse_*.deb  
RUN cd /tmp ; echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst  
RUN cd /tmp ; dpkg-deb -b . /fuse.deb  
RUN cd /tmp ; dpkg -i /fuse.deb  
RUN apt-get install -y ia32-libs-multiarch  
  
# Add git  
RUN apt-get install -y git-core  
  
# Add Jenkins  
# Thanks to orchardup/jenkins Dockerfile  
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key
add -  
RUN echo "deb http://pkg.jenkins-ci.org/debian-stable binary/" >>
/etc/apt/sources.list  
RUN apt-get update  
# HACK: https://issues.jenkins-ci.org/browse/JENKINS-20407  
RUN mkdir /var/run/jenkins  
RUN apt-get install -y jenkins  
RUN service jenkins stop  
EXPOSE 8080  
VOLUME ["/var/lib/jenkins"]  
ENTRYPOINT [ "java","-jar","/usr/share/jenkins/jenkins.war" ]  
## END  

