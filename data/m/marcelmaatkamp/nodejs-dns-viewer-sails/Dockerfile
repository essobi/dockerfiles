FROM node  
MAINTAINER m.maatkamp@gmail.com version: 0.1  
# ---  
# add libraries  
RUN npm install native-dns  
RUN npm install amqp  
RUN npm install -g node-gyp  
RUN npm install bson  
# RUN \cp -f node_modules/bson/ext/index.js
node_modules/bson/ext/index.js.orig; cat node_modules/bson/ext/index.js | sed
-e 's/..\/build\/Release\/bson/bson/g' | > node_modules/bson/ext/index.js.bak;
mv -f node_modules/bson/ext/index.js.bak node_modules/bson/ext/index.js  
RUN npm -g install sails  
RUN npm -g install sails-mongo --save  
RUN npm -g install grunt-cli  
RUN npm -g install grunt --save-dev  
  
# ---  
# add sources  
WORKDIR /data/dnsViewer  
COPY dnsViewer /data/dnsViewer  
RUN npm install  
  
ENTRYPOINT ["sails", "lift"]  

