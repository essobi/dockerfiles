# Setting the base to nodejs 7.7.3  
FROM node:7.7.3-alpine  
  
# Maintainer  
MAINTAINER Frode Sjovatsen  
  
#### Begin setup ####  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production && npm run build  
  
EXPOSE 3000  
# Startup  
ENTRYPOINT npm start

