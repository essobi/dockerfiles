FROM node:6  
MAINTAINER Praekelt.org <dev@praekelt.org>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ARG NODE_ENV  
ENV NODE_ENV $NODE_ENV  
  
COPY package.json /usr/src/app/  
  
RUN npm install \  
&& npm install plugin-node-tab  
  
COPY . /usr/src/app  
COPY /docker/plugin-node-tab/package.json /usr/src/app/node_modules/plugin-
node-tab/  
  
CMD ["./node_modules/.bin/gulp", "patternlab:serve"]  
  
EXPOSE 80

