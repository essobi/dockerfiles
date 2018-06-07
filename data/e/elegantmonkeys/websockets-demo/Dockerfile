FROM node:7-alpine  
  
EXPOSE 3000  
ENV NODE_ENV production  
  
RUN mkdir -p /opt/app  
WORKDIR /opt/app  
  
COPY package.json /opt/app  
RUN npm install  
COPY . /opt/app  
  
CMD ["npm", "start"]  

