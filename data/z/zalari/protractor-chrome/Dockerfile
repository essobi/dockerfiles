FROM node:6.2-slim  
MAINTAINER david.enke@zalari.de  
WORKDIR /tmp  
# install node dependencies  
RUN npm install -g \  
chai \  
chai-as-promised \  
jasmine \  
mocha \  
mocha-multi \  
mocha-proshot \  
protractor \  
protractor-screenshot-reporter  
RUN webdriver-manager update  
# install browser  
RUN apt-get update && apt-get install -y --force-yes \  
openjdk-7-jre \  
xvfb  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN dpkg --unpack google-chrome-stable_current_amd64.deb  
RUN apt-get install -f -y && apt-get clean  
RUN rm google-chrome-stable_current_amd64.deb  
# copy startup script  
COPY ./protractor.sh /protractor.sh  
# Fix for the issue with Selenium, as described here:  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
RUN mkdir /protractor  
WORKDIR /protractor  
ENTRYPOINT ["/protractor.sh"]  

