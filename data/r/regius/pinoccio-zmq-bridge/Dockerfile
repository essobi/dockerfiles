FROM node:5.4.1  
RUN mkdir -p /usr/src/app && apt-get update && apt-get install -y -q libzmq-
dev pkg-config  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
EXPOSE 22756  
CMD [ "node", "./server.js" ]  

