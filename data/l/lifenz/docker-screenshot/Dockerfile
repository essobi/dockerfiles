FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PHANTOM_JS_VERSION 2.1.1-linux-x86_64  
  
RUN apt-get update && \  
apt-get install -y curl bzip2 libfreetype6 libfontconfig && \  
curl -sSL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOM_JS_VERSION.tar.bz2
| tar xjC / && \  
ln -s phantomjs-$PHANTOM_JS_VERSION /phantomjs  
  
ADD ./rasterize.js /rasterize.js  
  
VOLUME ["/srv"]  
WORKDIR /srv  
  
ENTRYPOINT ["/phantomjs/bin/phantomjs", "/rasterize.js"]  

