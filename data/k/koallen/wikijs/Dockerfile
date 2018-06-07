FROM node:6.10.0-alpine  
  
RUN apk add --no-cache make gcc g++ python git  
  
WORKDIR /wiki-js  
RUN npm install wiki.js@latest  
  
EXPOSE 80  
CMD ["pm2-docker", "wiki", "start"]  

