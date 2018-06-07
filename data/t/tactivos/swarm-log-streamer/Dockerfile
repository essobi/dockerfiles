#Lightweight linux. 35mb vs 280 for standard node image  
FROM node:8-alpine  
  
RUN mkdir -p /app  
WORKDIR /app  
  
# Copy app to workdir  
COPY package.json /app/  
COPY index.* /app/  
  
RUN mkdir /app/static  
COPY static/* /app/static/  
  
#Install docker 17.05+  
#Edge repo, otherwise it would install docker 1.11 which has no swarm support  
COPY repositories /etc/apk/  
  
RUN apk update  
RUN apk add docker  
  
RUN npm install  
  
EXPOSE 3000  
ENTRYPOINT ["node", "index.js"]  

