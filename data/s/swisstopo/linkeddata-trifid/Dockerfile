FROM node:8  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
COPY . /usr/src/app  
RUN npm install && npm cache clean --force  
  
ENV NODE_ENV production  
  
RUN npm install pm2 -g  
CMD pm2-runtime start node_modules/.bin/trifid -- --config $TRIFID_CONFIG  
  
EXPOSE 8080  

