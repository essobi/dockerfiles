FROM node:8  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ARG NODE_ENV  
ENV NODE_ENV $NODE_ENV  
COPY package.json /usr/src/app/  
RUN npm install && npm cache clean --force  
COPY . /usr/src/app  
  
RUN mv .env.example .env  
RUN NODE_ENV=production ./node_modules/.bin/webpack  
  
CMD [ "npm", "start" ]  

