# This is a 2-phased Dockerfile  
# 1st phase builds the project  
# 2nd phase creates the distributable Docker-image  
FROM node:carbon-slim as build-env  
LABEL version="1.0"  
LABEL maintainer="Juha Ristolainen <juha.ristolainen@iki.fi>"  
LABEL author="Juha Ristolainen <juha.ristolainen@iki.fi>"  
  
# Install prerequisites  
RUN apt-get update -qq && apt-get install -y -qq curl git lftp wget  
  
# Use specific version to avoid building against a moving target. (never user
:latest in base images either)  
RUN npm install -g --no-optional @angular/cli@1.5.0  
  
COPY . /app  
WORKDIR /app  
  
# build the project  
RUN yarn install  
RUN yarn build --prod  
  
# Build runtime image  
FROM nginx:stable-alpine  
WORKDIR /app  
COPY \--from=build-env /app/dist /usr/share/nginx/html  
EXPOSE 80  

