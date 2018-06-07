# For more information; http://github.com/greatcloak/phantomgo  
#  
# phantomgo  
#  
# Usage  
# docker run greatcloak/phantomgo /usr/bin/phantomjs -v  
# docker run -v `pwd`:/mnt/test greatcloak/phantomgo /usr/bin/phantomjs
/mnt/test/test.js  
# VERSION 1.0.1  
FROM ubuntu:14.04  
MAINTAINER chadanded  
  
# Set environment variables.  
ENV GOROOT /usr/src/go  
ENV GOPATH /go  
ENV PATH $GOROOT/bin:$GOPATH/bin:$PATH  
  
# Install Go  
# Install some things we need  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install curl bzr git -y && \  
mkdir -p $GOROOT && \  
curl https://storage.googleapis.com/golang/go1.5.1.linux-amd64.tar.gz | tar
xvzf - -C $GOROOT \--strip-components=1  
  
# Define working directory.  
WORKDIR /go  
  
# Env  
ENV PHANTOMJS_VERSION 1.9.7  
# Commands  
RUN apt-get install -y vim git wget libfreetype6 libfontconfig bzip2 && \  
mkdir -p /srv/var && \  
wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y && \  
apt-get clean all  
  
# Default command  
CMD ["bash"]  

