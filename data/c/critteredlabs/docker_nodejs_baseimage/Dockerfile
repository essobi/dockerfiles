# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.18  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs  
  
#https://forums.couchbase.com/t/cannot-make-couchbase-node-js-sdk-working-
under-cenos-6-5/1128  
RUN apt-get -y install build-essential g++ less vim git wget libfreetype6
libfontconfig bzip2 python  
RUN npm install -g npm@latest  
RUN npm install -g node-gyp@latest  
RUN npm install -g aws-sdk@2.1.29 bluebird@2.9.5 bunyan@1.3.4 co@4.4.0
couchbase@latest flux@2.0.1 habitat@3.1.2 immutable@3.7.2 \  
intl@0.1.4 intl-messageformat@1.0.4 intl-relativeformat@1.0.3 koa@1.1.2 koa-
better-ratelimit@2.1.2 koa-body@1.2.1 \  
koa-bunyan-logger@1.2.0 koa-compress@1.0.8 koa-conditional-get@1.0.2 koa-
csrf@2.1.3 koa-error@1.1.3 bower \  
koa-etag@2.0.0 koa-favicon@1.2.0 koa-generic-session@1.6.0 koa-helmet@0.2.0
koa-locale@1.0.0 koa-memcached@0.1.2 \  
koa-passport@1.1.4 koa-qs@2.0.0 koa-router@4.3.2 koa-static@1.4.8 koa-
swig@2.0.0 lodash@3.10.1 longjohn@0.2.4 mailchimp-api@2.0.7 \  
mandrill-api@1.0.41 moment@2.9.0 node-uuid@1.4.2
git+https://github.com/visionmedia/page.js.git#master \  
passport-local@1.0.0 passport-twitter@1.0.3 qs@2.3.3 react@0.14.0 react-
dom@0.14.0 request@2.62.0 swig@1.4.2 twitter@1.2.1 useragent@2.1.5 \  
csv-parse@0.1.3 feedparser@1.1.1 htmlparser2@3.8.2 pm2 shelljs@0.5.3 tick
newrelic https://git@bitbucket.org/dreamrocket/radium.git \  
selenium-webdriver socketio  
RUN npm install -g iconv@2.1.11  
  
RUN /usr/sbin/update-rc.d cron defaults  
RUN wget https://download.elastic.co/logstash-forwarder/binaries/logstash-
forwarder_0.4.0_amd64.deb -O logstash-forwarder_0.4.0_amd64.deb && \  
dpkg -i logstash-forwarder_0.4.0_amd64.deb && \  
rm logstash-forwarder_0.4.0_amd64.deb  
  
ENV PHANTOMJS_VERSION 1.9.7  
RUN mkdir -p /srv/var  
RUN wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2  
RUN tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp  
RUN rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2  
RUN mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs  
RUN ln -s /srv/var/phantomjs/bin/phantomjs /usr/local/bin/phantomjs  
RUN git clone https://github.com/n1k0/casperjs.git /srv/var/casperjs  
RUN ln -s /srv/var/casperjs/bin/casperjs /usr/local/bin/casperjs  
  
ENV NODE_PATH /usr/local/lib/node_modules  
  
# Clean up APT when done.  
RUN apt-get autoremove -y  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Define working directory.  
WORKDIR /data  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

