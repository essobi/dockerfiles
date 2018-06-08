FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/usr/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 3123  
CMD [ "npm", "start" ]

