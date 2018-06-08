FROM debian:jessie  
MAINTAINER Abdulla Abdurakhmanov <abdulla.abd.m@gmail.com>  
  
# Docker registry for Debian  
RUN apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN apt-get update && apt-get install -y -qq apt-transport-https ca-
certificates gnupg2  
RUN echo "deb https://apt.dockerproject.org/repo debian-wheezy main" | tee
/etc/apt/sources.list.d/docker.list  
  
RUN apt-get update && apt-get install -y -qq --no-install-recommends curl
locales vim docker-engine mercurial python-software-properties rubygems ruby-
dev git build-essential  
  
# Locales  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# Java  
# update repos  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get update  
  
# install java  
RUN apt-get install oracle-java8-installer -y  
  
RUN apt-get clean  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ENV LANG=C.UTF-8 \  
LC_ALL=C.UTF-8 \  
LANGUAGE=C.UTF-8  
ENV SBT_VERSION 1.0.4  
ENV SBT_HOME /usr/local/sbt-launcher-packaging-${SBT_VERSION}  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
# SBT  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install -y bc sbt && \  
sbt sbtVersion  
  
WORKDIR /app  

