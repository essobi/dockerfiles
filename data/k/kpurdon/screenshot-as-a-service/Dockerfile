FROM node:0.12.5  
ENV PHANTOMJS_VERSION 1.9.6  
RUN wget --no-check-certificate -q -O -
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 | tar xjC /opt  
RUN ln -s /opt/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs
/usr/bin/phantomjs  
  
ADD . /usr/src/app  
WORKDIR /usr/src/app  
RUN npm install  
  
EXPOSE 3000  
ENTRYPOINT node app  

