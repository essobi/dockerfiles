FROM node:6.9.1-slim  
MAINTAINER Hideki Igarashi <hideki.develop@gmail.com>  
  
ENV ES_HEAD_REVISION b53d7a9dac0fadf4359af09af5866200b13c3942  
  
# for extracting the PhantomJS archive when `npm install`  
RUN apt-get update && \  
apt-get install -y bzip2 --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
RUN npm install -g grunt  
  
RUN useradd \  
\--home-dir /opt/elasticsearch-head \  
\--skel /dev/null \  
\--create-home \  
\--system \  
\--shell /bin/bash \  
es-head  
USER es-head  
  
WORKDIR /opt/elasticsearch-head  
  
RUN curl -L https://github.com/mobz/elasticsearch-
head/archive/$ES_HEAD_REVISION.tar.gz | \  
tar xvz --strip=1  
  
# upgrading grunt-contrib-connect to 1.0.2 for listen 0.0.0.0  
RUN npm set progress=false && \  
npm install -D grunt-contrib-connect@1.0.2 && \  
npm install && \  
rm -rf /tmp/phantomjs  
  
EXPOSE 9100  
# `grunt server` via `/bin/sh -c` because SIGINT is ineffective  
CMD grunt server  

