FROM ruby:2.3.5  
# Rebuild 20171212 083000  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
# Add yarn's package repository (from
<https://yarnpkg.com/en/docs/install#linux-tab>)  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update --assume-yes  
  
# to get latest npm for phantomjs  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
  
RUN apt-get install --assume-yes \  
build-essential nodejs \  
qt5-default libqt5webkit5-dev \  
xvfb \  
gstreamer1.0-plugins-base gstreamer1.0-tools gstreamer1.0-x \  
yarn \  
unzip  
  
# https://github.com/RobCherry/docker-chromedriver/blob/master/Dockerfile  
RUN CHROMEDRIVER_VERSION=`curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE` && \  
mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \  
curl -sS -o /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
&& \  
unzip -qq /tmp/chromedriver_linux64.zip -d
/opt/chromedriver-$CHROMEDRIVER_VERSION && \  
rm /tmp/chromedriver_linux64.zip && \  
chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \  
ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver
/usr/local/bin/chromedriver  
  
# https://github.com/ebidel/lighthouse-ci/blob/master/builder/Dockerfile  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - &&\  
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list' &&\  
apt-get update &&\  
apt-get install -y google-chrome-unstable  
  
# for phantom js (for jasmine tests for example) == depends on nodejs  
RUN npm install -g phantomjs-prebuilt  

