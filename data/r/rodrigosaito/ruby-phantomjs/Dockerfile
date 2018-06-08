FROM ruby:2.1.5  
  
MAINTAINER Rodrigo Saito <rodrigo.saito@gmail.com>  
  
# Add options to gemrc  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
  
# Install phantomjs  
# Env  
ENV PHANTOMJS_VERSION 1.9.8  
# Commands  
RUN \  
apt-get update && \  
apt-get install -y wget libfreetype6 libfontconfig bzip2 && \  
mkdir -p /srv/var && \  
wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \  
apt-get autoremove -y && \  
apt-get clean all  
  

