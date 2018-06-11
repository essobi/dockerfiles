FROM node:4.7.3-alpine  
  
COPY . /src  
WORKDIR /src  
  
RUN npm install npm@3 -g && npm install yarn -g && yarn install && yarn run
build-server  
  
CMD yarn run production  
  
EXPOSE 80  

