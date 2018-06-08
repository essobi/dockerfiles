FROM node:7-alpine  
  
ARG NODE_ENV  
ENV NODE_ENV $NODE_ENV  
  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
# install git for bower install  
RUN apk update && apk add git  
  
RUN npm install  
RUN ./node_modules/bower/bin/bower install --allow-root  
  
CMD [ "npm", "start" ]  
  

