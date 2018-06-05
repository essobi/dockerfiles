  
FROM node:8-alpine  
  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
  
ENV NODE_ENV=production  
  
RUN npm install  
  
EXPOSE 80  
CMD [ "node", "server" ]

