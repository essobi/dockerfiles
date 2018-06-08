# using v8.9.0 LTS  
FROM node:carbon  
  
ARG NODE_ENV=production  
ENV NODE_ENV $NODE_ENV  
  
# setup app working directory  
WORKDIR /usr/src/app  
  
# copy package and package-lock.json  
COPY package*.json ./  
  
# install app dependencies  
RUN npm install  
  
# copy the sourcecode  
COPY . .  
  
# start the app  
CMD [ "npm", "start" ]  

