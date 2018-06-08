FROM node:6.10-alpine  
  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
  
WORKDIR /usr/src/app  
RUN mkdir logs  
  
RUN npm install  
  
CMD [ "npm", "start" ]

