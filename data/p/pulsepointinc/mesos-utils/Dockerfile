FROM node:8-alpine  
  
WORKDIR /app  
COPY app/ /app/  
COPY package.json /app  
RUN apk add -U tzdata && npm --production install  
  
ENTRYPOINT [ "node", "/app/runner" ]  

