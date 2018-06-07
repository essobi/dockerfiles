###########################################################  
#  
# Dockerfile for tfk-opengov-meetings-extract  
#  
###########################################################  
  
# Setting the base to nodejs 4.6.0  
FROM mhart/alpine-
node:4.9.1@sha256:052772af605978749631e2b6d190c7d68dc607a480a6e4dbe84eaf7264759d2e  
  
# Maintainer  
MAINTAINER Geir Gåsodden  
  
#### Begin setup ####  
  
# Installs git  
RUN apk add --update git && rm -rf /var/cache/apk/*  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production  
  
# Startup  
ENTRYPOINT node index.js

