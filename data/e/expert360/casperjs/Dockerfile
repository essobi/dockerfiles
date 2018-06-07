FROM node:5  
  
ENTRYPOINT ["/usr/local/bin/casperjs"]  
  
ENV CASPER_VERSION=1.1.0-beta3 \  
PHANTOMJS_EXECUTABLE=/usr/local/lib/node_modules/casperjs/node_modules/phantomjs/lib/phantom/bin/phantomjs  
  
RUN npm install -g casperjs@${CASPER_VERSION}  

