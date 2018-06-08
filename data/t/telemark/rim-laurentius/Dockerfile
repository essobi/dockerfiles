###########################################################  
#  
# Dockerfile for the-real-laurentius  
#  
###########################################################  
  
# Setting the base to nodejs 7.4.0  
FROM node:7.4.0-alpine  
  
# Maintainer  
MAINTAINER Jonas Enge  
  
#### Begin setup ####  
  
# Installs git  
RUN apk add --update --no-cache git  
  
# Extra tools for native dependencies  
RUN apk add --no-cache make gcc g++ python  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production  
  
# Startup  
ENTRYPOINT node index.js  

