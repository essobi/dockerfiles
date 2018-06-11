FROM node:6.9.4-slim  
MAINTAINER j.ciolek@webnicer.com  
WORKDIR /tmp  
COPY webdriver-versions.js ./  
ENV CHROME_PACKAGE="google-chrome-stable"
NODE_PATH=/usr/local/lib/node_modules:/protractor/node_modules  
RUN npm install -g protractor@4.0.14 minimist@1.2.0 && \  
node ./webdriver-versions.js --chromedriver 2.32 && \  
webdriver-manager update  
  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list.d/jessie-backports.list  
RUN apt-get update && \  
apt-get install -y xvfb wget sudo && \  
apt-get install -y -t jessie-backports openjdk-8-jre && \  
apt-get install -y --force-yes ${CHROME_PACKAGE}  
ENV CHROME_BIN /usr/bin/google-chrome  
  
RUN mkdir /protractor  
COPY protractor.sh /  
  
COPY environment /etc/sudoers.d/  
# Fix for the issue with Selenium, as described here:  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null SCREEN_RES=1280x1024x24  
WORKDIR /protractor  
ENTRYPOINT ["/protractor.sh"]  

