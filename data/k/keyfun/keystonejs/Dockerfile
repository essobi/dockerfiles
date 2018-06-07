FROM node:6.9.4  
MAINTAINER Key <keyfun.hk@gmail.com>  
  
ENV KEYSTONEJS_VERSION 4.0.0-beta.4  
ENV NODE_MODULE_INSTALLATION_PATH /usr/src/modules  
ENV NODE_PATH $NODE_MODULE_INSTALLATION_PATH/node_modules  
  
RUN mkdir -p $NODE_MODULE_INSTALLATION_PATH  
WORKDIR $NODE_MODULE_INSTALLATION_PATH  
  
# FIX on npm3 https://github.com/npm/npm/issues/9863  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs\\.move/
./lib/utils/rename.js  
  
RUN npm install dotenv@1.2.0  
RUN npm install jade@1.11.0  
RUN npm install keystone@$KEYSTONEJS_VERSION  
  
WORKDIR /usr/src/app  
  
EXPOSE 3000 3001  
CMD [ "node", "keystone.js" ]  

