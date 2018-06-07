FROM node  
MAINTAINER Sawood Alam <ibnesayeed@gmail.com>  
  
RUN npm install faye  
  
ENV PORT=8000 TIMEOUT=45 MOUNT=/faye  
  
ADD ./app /app  
  
WORKDIR /app  
  
ENTRYPOINT node server.js  

