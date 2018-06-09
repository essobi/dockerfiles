FROM node:latest  
  
MAINTAINER Paolo Chiabrera <paolo.chiabrera@gmail.com>  
  
# currently only works for development  
ENV NODE_ENV develop  
  
ENV NODE_PORT 9020  
ENV PM2_HOME /home/app/.pm2  
  
# install graphicsmagick  
RUN apt-get update -y  
  
RUN apt-get install -y graphicsmagick  
  
# use changes to package.json to force Docker not to use the cache  
# when we change our application's nodejs dependencies:  
ADD package.json /tmp/package.json  
  
RUN cd /tmp && npm install --save pm2@latest -g && npm install --production  
  
RUN mkdir -p /home/app && cp -a /tmp/node_modules /home/app  
  
RUN pm2 startup ubuntu  
  
WORKDIR /home/app  
  
ADD . /home/app  
  
CMD pm2 start /home/app/index.js -x -i 1 --name pmp_thumbs_api && pm2 save &&
pm2 logs

