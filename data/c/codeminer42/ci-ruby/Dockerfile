FROM ruby:2.1  
MAINTAINER Carlos Lopes <carlos.lopes@codeminer42.com>  
  
# Add Google Chrome PPA  
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list  
  
# Install dependencies  
RUN apt-get -yqq update && \  
apt-get -yqq install --no-install-recommends \  
git \  
libfreetype6 \  
libfontconfig \  
bzip2 \  
qt5-default \  
libqt5webkit5-dev \  
gstreamer1.0-plugins-base \  
gstreamer1.0-tools \  
gstreamer1.0-x \  
google-chrome-stable \  
xvfb \  
unzip \  
fonts-ipafont-gothic xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-
cyrillic \  
xauth && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Chrome WebDriver  
RUN CHROMEDRIVER_VERSION=2.37 && \  
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
  
# Default configuration  
ENV DISPLAY :20.0  
ENV SCREEN_GEOMETRY "1920x1080x24"  
ENV CHROMEDRIVER_PORT 4444  
ENV CHROMEDRIVER_WHITELISTED_IPS "127.0.0.1"  
ENV CHROMEDRIVER_URL_BASE ''  
# Install Phantom.js  
ENV PHANTOMJS_VERSION 2.1.1  
RUN mkdir -p /srv/var  
RUN curl -sSLO
"https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2" && \  
tar -xjf "phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2" -C "/tmp" && \  
rm -f "phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2" && \  
mv "/tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/" /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs  
  
# Install node / npm  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 8.11.1  
RUN curl -sSLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" && \  
tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 && \  
rm -f "node-v$NODE_VERSION-linux-x64.tar.xz" && \  
npm install npm -g  

