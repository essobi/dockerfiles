FROM node:latest  
  
ARG port=4000  
WORKDIR /src  
  
COPY package.json /src  
RUN npm install  
  
COPY . /src  
  
#EXPOSE 4000  
EXPOSE $port  
  
CMD ["node", "node_server.js"]

