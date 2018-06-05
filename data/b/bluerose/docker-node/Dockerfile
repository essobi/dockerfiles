FROM node:8.2.1  
ENV CHROME_PACKAGE="google-chrome-stable_60.0.3112.90-1_amd64.deb"  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y -t jessie-backports openjdk-8-jre  
  
RUN wget https://github.com/webnicer/chrome-
downloads/raw/master/x64.deb/${CHROME_PACKAGE} && \  
dpkg --unpack ${CHROME_PACKAGE} && \  
apt-get install -f -y && \  
apt-get clean && \  
rm ${CHROME_PACKAGE}  
  
# Fix for the issue with Selenium, as described here:  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null SCREEN_RES=1280x1024x24

