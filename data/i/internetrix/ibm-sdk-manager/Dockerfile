FROM ubuntu:latest  
MAINTAINER Jason Zhang <jason.zhang@internetrix.com.au>  
ARG DEBIAN_FRONTEND=noninteractive  
  
### Change to default mirror to AU mirror -
https://wiki.ubuntu.com/AustralianTeam/LocalAptMirrors#Australian_Mirrors  
RUN sed -i -e 's/http:\/\/archive./http:\/\/au.archive./g'
/etc/apt/sources.list && \  
sed -i -e 's/http:\/\/releases./http:\/\/au.releases./g' /etc/apt/sources.list  
  
### SET UP  
RUN apt-get -qq update  
  
# Supporting tools  
RUN apt-get -qqy install git wget nano vim curl git zip unzip locales
software-properties-common  
  
RUN echo "LANG=en_US.UTF-8\n" > /etc/default/locale && \  
echo "en_US.UTF-8 UTF-8\n" > /etc/locale.gen && \  
locale-gen  
  
ENV ENV LANG en_US.UTF-8  
# NodeJS and common global NPM modules  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get -qqy install nodejs  
  
# IBM SDK Manage only works for npm@5.4.1 version  
RUN npm install -g npm@5.4.1  
  
# install Java JDK  
RUN apt-get -qqy install default-jdk  
  
# install Ruby  
RUN apt-get -qqy install ruby  
  
# get IBM SDK Manager from github  
RUN cd && \  
git clone https://github.com/ibm-watson-cxa/SDK_Tools.git ibm_sdk_tools  

