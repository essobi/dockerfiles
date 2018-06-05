FROM node:latest  
  
# monitor server js change  
RUN npm install nodemon -g  
RUN npm install -g node-inspector  
  
# Create app directory  
RUN mkdir -p /app/math/src  
WORKDIR /app/math/src  
  
# Install app dependencies  
COPY package.json /app/math/src  
RUN npm install  
  
# Bundle app source  
COPY . /app/math/src  
  

