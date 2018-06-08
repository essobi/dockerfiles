FROM node:8-slim  
MAINTAINER rafael@meupatrocinio.com  
WORKDIR /tmp  
COPY webdriver-versions.js ./  
ENV CHROME_PACKAGE="google-chrome-stable_67.0.3396.62-1_amd64.deb"
NODE_PATH=/usr/local/lib/node_modules:/protractor/node_modules  
RUN mkdir -p /usr/share/man/man1 \  
&& mkdir -p /usr/share/man/man7  
RUN npm install -g protractor minimist && \  
node ./webdriver-versions.js --chromedriver 2.39 && \  
webdriver-manager update && \  
echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y xvfb wget sudo && \  
apt-get install -y -t jessie-backports openjdk-8-jre && \  
wget https://github.com/webnicer/chrome-
downloads/raw/master/x64.deb/${CHROME_PACKAGE} && \  
dpkg --unpack ${CHROME_PACKAGE} && \  
apt-get install -f -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
rm ${CHROME_PACKAGE} && \  
mkdir /protractor  
COPY protractor.sh /  
COPY environment /etc/sudoers.d/  
# Fix for the issue with Selenium, as described here:  
# https://github.com/SeleniumHQ/docker-selenium/issues/87  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null SCREEN_RES=1280x1024x24  
WORKDIR /protractor  
ENTRYPOINT ["/protractor.sh"]  

