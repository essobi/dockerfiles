FROM elixir:1.3  
MAINTAINER Oren Kanner <okanner@gmail.com>  
  
ENV PHANTOMJS_VERSION 2.1.1  
  
RUN set -xe && apt-get update && \  
apt-get upgrade -y && \  
cd /tmp && \  
curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 | tar jx && \  
cp phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs /usr/bin/ && \  
rm -rf /tmp/* && \  
apt-get autoremove -y && \  
apt-get clean all  

