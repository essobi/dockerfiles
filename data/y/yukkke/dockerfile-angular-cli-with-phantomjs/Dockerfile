FROM node:8.11.1  
MAINTAINER yukkke <Yusuke Yasuo> "yasuo.yusuke@redish.jp"  
ENV NPM_VERSION 5.8.0  
ENV PHANTOM_JS_VERSION 2.1.1-linux-x86_64  
  
RUN npm install -g npm@$NPM_VERSION  
RUN npm install -g @angular/cli  
  
RUN apt-get update  
RUN apt-get install -y curl bzip2 libfreetype6 libfontconfig  
  
RUN curl -sSL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOM_JS_VERSION.tar.bz2
| tar xjC /  
RUN ln -s phantomjs-$PHANTOM_JS_VERSION/bin/phantomjs /usr/local/bin/phantomjs  

