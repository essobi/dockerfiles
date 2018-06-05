FROM node:4.2  
MAINTAINER ewere <ediagboya@terragonltd.com>  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
COPY . /usr/src/app/  
  
CMD ["npm", "start"]

