FROM node  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install --production && npm cache clean --force  
COPY . /usr/src/app  
  
CMD [ "npm", "start" ]  

