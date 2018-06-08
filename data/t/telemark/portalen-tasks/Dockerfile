###########################################################  
#  
# Dockerfile for tasks-front  
#  
###########################################################  
  
# Setting the base to nodejs 8.5.0  
FROM node:8.5.0-alpine  
  
# Maintainer  
MAINTAINER Geir Gåsodden  
  
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
  
EXPOSE 8000  
  
# Startup  
CMD ["node", "server.js"]  

