FROM node:6  
## Create and move to app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app/  
  
ARG SERVER_ENV="PROD"  
ARG NODE_ENV="production"  
ENV SERVER_ENV=${SERVER_ENV}  
ENV NODE_ENV=${NODE_ENV}  
  
## Assume NPM_TOKEN is in environment or provided by docker-compose file,
create .npmrc using NPM_TOKEN  
ARG NPM_TOKEN  
RUN echo "//registry.npmjs.org/:_authToken=${NPM_TOKEN}" > .npmrc  
  
## Install app dependencies - production deps only (--production is default
when NODE_ENV=production)  
RUN npm install -y --production  
  
## Bundle app source in destination (NOTE .dockerignore applies here)  
COPY . /usr/src/app  
  
## Clean up non-prod dependencies  
RUN npm prune --production  
  
EXPOSE 8120  
CMD npm start  

