FROM node:latest  
  
MAINTAINER salihigde@gmail.com  
  
RUN mkdir -p /src/nodeapp  
WORKDIR /src/nodeapp  
  
COPY package.json /src/nodeapp  
RUN npm install  
COPY . /src/nodeapp  
  
EXPOSE 8080  
CMD ["node", "server.js"]

