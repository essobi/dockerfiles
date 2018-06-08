FROM node:0.12.7  
  
RUN mkdir -p /dist/node_modules  
ADD package.json /dist/package.json  
  
RUN npm install -g gulp-cli && npm install \--prefix=/dist  
ENV NODE_PATH=/dist/node_modules:/usr/local/lib/node_modules  
  
ADD . /code/client  
WORKDIR /code/client  
  
EXPOSE 8001  
  
CMD gulp build --production && env NODE_ENV=server node server.js  

