###########################################################  
#  
# Dockerfile for Portalen  
#  
###########################################################  
  
# Setting the base to nodejs 4.4.3  
FROM mhart/alpine-node:4.4.3  
  
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
  
# Env variables  
ENV SERVER_PORT 3000  
  
# Expose 3000  
EXPOSE 3000  
  
# Startup  
ENTRYPOINT node standalone.js

