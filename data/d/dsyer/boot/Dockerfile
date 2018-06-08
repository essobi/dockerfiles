FROM ubuntu:latest  
  
MAINTAINER dsyer@gopivotal.com  
  
RUN echo 'deb http://archive.ubuntu.com/ubuntu/ precise universe' >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y bash-completion curl zip wget git-core  
  
ENV HOME /root  
  
# Fake installation of fuse to allow JDK to install  
RUN apt-get install libfuse2  
RUN cd /tmp ; apt-get download fuse; dpkg-deb -x fuse_* .; dpkg-deb -e fuse_*;
rm fuse_*.deb; echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst; dpkg-deb -b
. /fuse.deb; dpkg -i /fuse.deb  
  
# Java  
RUN apt-get install -y openjdk-7-jdk; rm -rf /tmp/* /fuse.deb  
  
# GVM  
RUN curl -s get.gvmtool.net | bash  
RUN echo '[[ -s "$HOME/.bash_profile ]] && source "$HOME/.bash_profile"' >>
/etc/profile.d/gvm.sh  
  
# Maven  
# (The debian package sucks massively, so download directly)  
RUN cd /tmp; wget
http://mirror.gopotato.co.uk/apache/maven/maven-3/3.0.5/binaries/apache-
maven-3.0.5-bin.tar.gz  
RUN cd /opt; tar -xzf /tmp/apache-maven-3.0.5-bin.tar.gz; mv apache-
maven-3.0.5 maven; ln -s /opt/maven/bin/mvn /usr/local/bin; rm -rf /tmp/*  
  
# Pre-populate Maven cache with some useful stuff  
RUN [ ! -s /root/spring-boot ] && git clone https://github.com/spring-
projects/spring-boot /root/spring-boot  
RUN cd /root/spring-boot; git pull --rebase; mvn install -DskipTests=true  
  

