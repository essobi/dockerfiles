###########################################################  
#  
# Dockerfile for minelev-buddy  
#  
###########################################################  
  
# Setting the base to nodejs 7.7.2  
FROM node:7.7.2-alpine  
  
# Maintainer  
MAINTAINER Geir Gåsodden  
  
#### Begin setup ####  
  
# Installs git  
RUN apk add --update --no-cache git  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production  
  
# Expose 3000  
EXPOSE 3000  
  
# Startup  
ENTRYPOINT npm start

