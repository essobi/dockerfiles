FROM node:slim  
MAINTAINER Edgard Aviles "edgard.aviles@ooqia.com"  
ENV UPDATED_AT 2017-01-21  
WORKDIR /tmp  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  
  
RUN apt-get update -qqy && \  
echo "oracle-java7-installer shared/accepted-oracle-license-v1-1 select true"
| /usr/bin/debconf-set-selections && \  
apt-get update -qqy && apt-get install -qqy oracle-java7-installer oracle-
java7-set-default  
  
RUN apt-get install -qqy xvfb wget net-tools && \  
npm install -g protractor mocha jasmine && \  
webdriver-manager update && \  
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
&& \  
dpkg --unpack google-chrome-stable_current_amd64.deb && \  
apt-get install -f -y && \  
apt-get clean && \  
rm google-chrome-stable_current_amd64.deb && \  
mkdir /protractor  
ADD protractor.sh /protractor.sh  
ADD xvfb-run-safe /usr/bin/  
RUN chmod +x /usr/bin/xvfb-run-safe  
RUN chmod +x /protractor.sh  
# Fix for the issue with Selenium, as described here:  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
ENV SCREEN_RES=1280x1024x24  
ENV SERVERNUM=1  
WORKDIR /protractor  
ENTRYPOINT ["/protractor.sh"]  

