FROM node:9.5.0-alpine  
  
# Install node_modules outside our mount  
WORKDIR /usr/src  
COPY package*.json ./  
# RUN npm install  
RUN npm install --quiet  
ENV NODE_PATH=/usr/src/node_modules  
  
WORKDIR /usr/src/app  
COPY . .

