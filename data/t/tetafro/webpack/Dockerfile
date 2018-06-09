FROM node:latest  
LABEL maintainer="Denis Ivanov"  
  
RUN npm install webpack -g  
  
VOLUME "/app"  
  
WORKDIR /app  
  
ENTRYPOINT [ "webpack" ]  

