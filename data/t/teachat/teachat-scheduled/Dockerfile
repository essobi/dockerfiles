FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/src/teachat-scheduled  
WORKDIR /usr/src/teachat-scheduled  
  
# Install app dependencies  
COPY . /usr/src/teachat-scheduled  
  
RUN npm install  
  
CMD [ "npm", "start" ]

