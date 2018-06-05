FROM node:7  
RUN mkdir -p /usr/app  
COPY . /usr/app  
WORKDIR /usr/app  
RUN npm install --production  
  
CMD ["npm", "start"]  

