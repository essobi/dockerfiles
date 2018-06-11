FROM ubuntu:trusty  
  
# Upgrading the new image  
RUN \  
apt-get -y update && \  
apt-get install -y apt-transport-https \  
build-essential \  
bzip2 \  
python2.7-dev \  
software-properties-common \  
curl \  
wget \  
make  
  
# Install Node.js  
RUN \  
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
  
RUN \  
apt-get update && \  
apt-get install -y nodejs  
  
# Install Stable NPM  
RUN \  
npm install npm@5  
  
# Install Phantom.js  
ENV PHANTOMJS_VERSION 1.9.8  
RUN \  
apt-get install -y libfreetype6 libfontconfig && \  
wget -q
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar xjf phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
install -t /usr/local/bin phantomjs-$PHANTOMJS_VERSION-
linux-x86_64/bin/phantomjs && \  
rm -rf phantomjs-$PHANTOMJS_VERSION-linux-x86_64 && \  
rm phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2

