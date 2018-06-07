FROM ubuntu:trusty  
  
# Debian package configuration use the noninteractive frontend.  
# http://manpages.ubuntu.com/manpages/wily/man7/debconf.7.html  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qqy \  
&& apt-get install -y \  
apt-utils \  
wget \  
sudo \  
curl  
  
# Font libraries  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
fonts-ipafont-gothic \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
xfonts-scalable \  
ttf-ubuntu-font-family \  
libfreetype6 \  
libfontconfig  
  
# Nodejs 6 with npm install  
# https://github.com/nodesource/distributions#installation-instructions  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
software-properties-common \  
python-software-properties  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
nodejs \  
build-essential  
  
# Latest Google Chrome installation package  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list'  
  
# Latest Ubuntu XVFB, Firefox, Google Chrome and JRE installs  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
xvfb \  
firefox\  
google-chrome-stable \  
default-jre  
  
RUN sudo apt-mark hold firefox  
  
# Clean clears out the local repository of retrieved package files. Run apt-
get clean from time to time to free up disk space.  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# 1. Step to fixing the error for Node.js native addon build tool (node-gyp)  
# https://github.com/nodejs/node-gyp/issues/454  
# https://github.com/npm/npm/issues/2952  
RUN rm -fr /root/tmp  
  
# Jasmine and protractor global install  
RUN npm install --unsafe-perm --save-exact -g protractor@5.2.0 \  
# Get the latest Google Chrome driver  
&& npm update \  
# Get the latest WebDriver Manager  
&& webdriver-manager update  
  
# Set the path to the global npm install directory. This is vital for Jasmine
Reporters  
ENV NODE_PATH /usr/lib/node_modules  
# Global reporters for protractor  
RUN npm install --unsafe-perm -g \  
jasmine-reporters \  
jasmine-spec-reporter \  
protractor-jasmine2-html-reporter \  
jasmine-allure-reporter \  
protractor-console

