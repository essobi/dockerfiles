FROM node:6.3.0  
MAINTAINER eliasbf@openmialbox.org  
  
# Install requirements for run automated test with selenium  
RUN apt-get update && \  
apt-get install -y pkg-mozilla-archive-keyring debian-keyring  
  
RUN echo "deb http://mozilla.debian.net/ jessie-backports firefox-release" >>
/etc/apt/sources.list  
RUN echo "deb-src http://mozilla.debian.net/ jessie-backports firefox-release"
>> /etc/apt/sources.list  
RUN echo "deb http://ftp.de.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y -t jessie-backports firefox && \  
apt-get install -y xvfb && \  
apt-get install -y openjdk-8-jdk && \  
apt-get install -y chromium && \  
apt-get install -y chromedriver  
  
# Retrieve selenium server  
RUN mkdir -p /opt  
RUN wget --no-verbose -O /opt/selenium-server-standalone-2.53.0.jar
http://selenium-release.storage.googleapis.com/2.53/selenium-server-
standalone-2.53.0.jar  
  
# Install requirements for run automated tests in polymer  
RUN npm install -g bower  
RUN npm install -g polymer-cli  
  
# Configure environment  
ENV DISPLAY :10  
# Specifies where given browser is installed (required for launchpad in
polymer tests)  
# (Solution to possible error starting polymer test)  
ENV LAUNCHPAD_CHROME=/usr/bin/chromium  
ENV LAUNCHPAD_FIREFOX=/usr/bin/firefox  

