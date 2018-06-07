FROM dockerfile/nodejs  
MAINTAINER m.maatkamp@gmail.com version: 0.1  
# ---  
# add libraries  
RUN npm install mongodb  
RUN npm install amqplib  
RUN npm install -g node-gyp  
RUN npm install bson  
  
# /data/node_modules/bson/node_modules/bson-ext/ext/index.js  
RUN \cp -f /data/node_modules/bson/node_modules/bson-ext/ext/index.js
/data/node_modules/bson/node_modules/bson-ext/ext/index.js.orig; cat
/data/node_modules/bson/node_modules/bson-ext/ext/index.js | sed -e
's/..\/build\/Release\/bson/bson/g' >
/data/node_modules/bson/node_modules/bson-ext/ext/index.js.bak; mv -f
/data/node_modules/bson/node_modules/bson-ext/ext/index.js.bak
/data/node_modules/bson/node_modules/bson-ext/ext/index.js  
  
# ---  
# add sources  
ADD js .  
  
ENTRYPOINT ["node", "/data/mongodb.js"]  

