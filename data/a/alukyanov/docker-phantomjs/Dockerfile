FROM ruby:2.2.3  
  
MAINTAINER rudarberry  
  
ENV PHANTOMJS_VERSION 2.1.1  
  
RUN mkdir -p /srv/var && \  
curl -SLO /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /usr/local/share/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C
/tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \  
phantomjs --version  

