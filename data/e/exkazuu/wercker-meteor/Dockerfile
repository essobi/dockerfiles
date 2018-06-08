FROM debian:jessie  
MAINTAINER Kazunori Sakamoto <exkazuu@gmail.com>  
  
ENV NODE_VERSION 4.5.0  
ENV PHANTOMJS_VERSION 2.1.1  
# Preparation  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
build-essential \  
git \  
python \  
graphicsmagick \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install program to configure locales  
RUN apt-get update && apt-get install -y --no-install-recommends \  
locales \  
&& dpkg-reconfigure locales \  
&& locale-gen C.UTF-8 \  
&& /usr/sbin/update-locale LANG=C.UTF-8 \  
&& apt-get purge -y --auto-remove locales \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
# Install Node.js  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" \  
&& npm cache clear  
  
# Install PhantomJS  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
libfontconfig \  
&& mkdir /tmp/phantomjs \  
&& curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 \  
| tar -xj --strip-components=1 -C /tmp/phantomjs \  
&& cd /tmp/phantomjs \  
&& mv bin/phantomjs /usr/local/bin \  
&& cd \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Meteor  
RUN curl https://install.meteor.com | sh  
  
# Install Meteor Up  
RUN npm install -g mup  
  
# Install Gem  
RUN apt-get update && apt-get install -y --no-install-recommends \  
rubygems \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Clean up  
RUN apt-get purge -y --auto-remove curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN node --version \  
&& npm \--version \  
&& meteor --version \  
&& phantomjs --version \  
&& gem --version  

