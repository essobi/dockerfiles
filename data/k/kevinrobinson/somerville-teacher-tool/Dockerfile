FROM node:4.2.2  
RUN npm install -g webpack  
  
COPY package.json /mnt/webpack/  
WORKDIR /mnt/webpack  
RUN npm install  
  
COPY . /mnt/webpack/

