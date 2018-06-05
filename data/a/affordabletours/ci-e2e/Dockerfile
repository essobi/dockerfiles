# Based on https://hub.docker.com/r/grme/nightwatch-chrome-firefox/  
FROM ubuntu:latest  
MAINTAINER Claas Augner "github@caugner.de"  
# update apt-get  
RUN apt-get -y update \  
&& apt-get -y upgrade  
  
# apt-utils  
RUN apt-get -y install apt-utils  
  
# nano  
RUN apt-get -y install nano  
  
# Git  
RUN apt-get -y install git  
  
# Java  
RUN apt-get -y --no-install-recommends install openjdk-8-jre-headless  
  
# curl  
RUN apt-get -y install curl  
  
# wget, bzip2  
RUN apt-get -y install wget bzip2  
  
# Node.  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get -y install nodejs \  
&& npm install npm@latest -g  
  
# xvfb  
RUN apt-get -y install xvfb  
  
# Chrome.  
ARG CHROME_VERSION="google-chrome-stable"  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -y install ${CHROME_VERSION:-google-chrome-stable} \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# Firefox.  
ARG FIREFOX_VERSION=55.0.2  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install firefox \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& apt-get -y purge firefox \  
&& rm -rf /opt/firefox \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \  
&& ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox  

