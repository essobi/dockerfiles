# File: Dockerfile  
#  
# Author: Massimo Cannavo <massimo5cannavo@gmail.com>  
# Date: Sun May 6 19:12:57 PDT 2018  
#  
# Dockerfile that builds the Node.js Express App from the Udemy Docker  
# Mastery course.  
#  
# https://github.com/BretFisher/udemy-docker-mastery  
#  
# Usage: docker container run --detach --publish 80:3000 massimocannavo/webapp  
FROM node:6-alpine  
  
# Default node environment is production.  
ARG NODE_ENV=production  
ENV NODE_ENV $NODE_ENV  
  
WORKDIR /usr/src/app  
COPY package.json ./  
  
# Install app dependencies.  
RUN npm install && npm cache clean --force  
COPY . .  
  
EXPOSE 3000  
HEALTHCHECK CMD wget -qs http://localhost:3000 || exit 1  
  
USER node  
CMD ["node", "./bin/www"]  

