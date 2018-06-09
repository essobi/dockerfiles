# Setting the base to nodejs 8.6.0  
FROM
node:8.11.1-alpine@sha256:dcee83ad53ab1d2754ca7029a06aa1f2c79bf3ee08b1a40bb052443efacd3b8f  
  
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
  
# Startup  
ENTRYPOINT node example.js  

