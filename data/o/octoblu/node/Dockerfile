FROM node:7-alpine  
MAINTAINER Octoblu <docker@octoblu.com>  
  
ENV NPM_CONFIG_LOGLEVEL error  
  
RUN apk add --no-cache alpine-sdk python-dev  
  
# Fix bug https://github.com/npm/npm/issues/9863  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js  
  
RUN npm --silent install node-gyp -g && node-gyp install && npm cache clean  

