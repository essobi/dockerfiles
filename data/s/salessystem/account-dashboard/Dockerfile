FROM clojure:alpine  
  
MAINTAINER Baiyuan Wang <wangbaiyuan@outlook.com>  
  
ENV PHANTOMJS_VERSION 2.1.1  
ENV LANG en_US.utf8  
  
RUN apk add --no-cache git curl fontconfig ttf-dejavu  
WORKDIR /dockerTmp  
RUN echo "Downloading PhantomJS v${PHANTOMJS_VERSION}..." && \  
curl -sL
"https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2"
| tar jx && \  
mv phantomjs-${PHANTOMJS_VERSION}-linux-x86_64 /tmp/phantomjs && \  
ln -s /tmp/phantomjs/bin/phantomjs /usr/bin/phantomjs && \  
echo "Fixing PhantomJS on Alpine" && \  
curl -sL
"https://github.com/dustinblackman/phantomized/releases/download/${PHANTOMJS_VERSION}/dockerized-
phantomjs.tar.gz" | tar zx -C / && \  
apk del git curl && rm -rf /dockerTmp  
  
WORKDIR /docker  
  
ADD project.clj .  
RUN lein deps  
  

