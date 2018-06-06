FROM node:slim  
MAINTAINER david.enke@zalari.de  
WORKDIR /tmp  
# install browser  
RUN sh -c 'echo "deb http://packages.linuxmint.com debian import" >>
/etc/apt/sources.list' && \  
apt-get update && \  
apt-get install -y --force-yes xvfb wget openjdk-7-jre chromium && \  
apt-get clean  
# install node dependencies  
RUN npm install -g protractor protractor-screenshot-reporter mocha mocha-multi
mocha-proshot chai chai-as-promised  
RUN webdriver-manager update  
RUN mkdir /protractor  
# copy startup script  
COPY ./protractor.sh /protractor.sh  
# Fix for the issue with Selenium, as described here:  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
WORKDIR /protractor  
ENTRYPOINT ["/protractor.sh"]  

