FROM node:9-alpine  
  
COPY . /app  
  
RUN ls /app  
  
RUN cd /app/client && yarn install && yarn build  
RUN cd /app/server && yarn install && ln -s ../client/dist public  
  
WORKDIR /app/server  
  
CMD node server.js

