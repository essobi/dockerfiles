FROM node:6.9.4-alpine  
  
# Create app directory  
RUN mkdir -p /home/app  
RUN mkdir -p /home/app/test  
RUN mkdir -p /home/app/ping-service  
WORKDIR /home/app  
  
# Install app dependencies  
COPY package.json /home/app/ping-service  
RUN cd ping-service && npm install;  
  
# Bundle app source  
COPY . /home/app/ping-service  
  
CMD cd ping-service ; npm start

