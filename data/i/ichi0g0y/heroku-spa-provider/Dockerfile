FROM mhart/alpine-node-auto:6.2.0  
# author  
MAINTAINER Shinichi Yamashita <ichi0g0y [at] gmail.com>  
  
# add and copy  
WORKDIR /srv/node  
ADD ./server.js /srv/node/server.js  
ADD ./package.json /srv/node/package.json  
RUN npm i --production  
  
# launch  
CMD ["npm", "start"]  

