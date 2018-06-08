# Minimal docker container to build project  
FROM ubuntu:xenial  
MAINTAINER positron96  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install updates & requirements:  
RUN apt-get -qq update && apt-get -qq dist-upgrade && apt-get install -qq -y
--no-install-recommends \  
git \  
openssh-client \  
ca-certificates \  
&& apt-get -qq clean  
  
RUN apt-get install -y openjdk-8-jdk && apt-get -qq clean  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN apt-get install -y ant && apt-get -qq clean  
  
RUN echo 'root:root' | chpasswd  
  
WORKDIR /root  

