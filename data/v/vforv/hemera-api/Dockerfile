FROM node:6.9.4-alpine  
  
# Create app directory  
RUN mkdir -p /home/app  
RUN mkdir -p /home/app/test  
RUN mkdir -p /home/app/api-gateway  
WORKDIR /home/app  
  
# Install app dependencies  
COPY package.json /home/app/api-gateway  
RUN cd api-gateway && npm install;  
  
# Bundle app source  
COPY . /home/app/api-gateway  
  
CMD cd api-gateway ; npm start

