FROM node:alpine  
RUN apk add \--no-cache tini  
COPY . /src/app  
WORKDIR /src/app  
RUN npm install && npm run prepublish  
USER node  
ENTRYPOINT ["/sbin/tini","--","node","server.js"]  

