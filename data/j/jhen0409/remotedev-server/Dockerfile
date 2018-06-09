# VERSION 1.0.0  
# AUTHOR: Jhen <developer@jhen.me>  
# DESCRIPTION: RemoteDev Server image  
# TO_BUILD: docker build --rm -t jhen0409/remotedev-server .  
# SOURCE: https://github.com/jhen0409/docker-remotedev-server  
FROM node:6  
MAINTAINER Jhen <developer@jhen.me>  
  
ADD . /remotedev  
WORKDIR /remotedev  
  
RUN npm install --production  
  
CMD ["npm", "start"]  

