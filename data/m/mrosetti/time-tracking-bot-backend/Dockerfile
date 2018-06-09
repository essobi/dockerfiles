  
FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/src/ttb-backend  
WORKDIR /usr/src/ttb-backend  
  
# Install app dependencies  
COPY . /usr/src/ttb-backend  
  
RUN npm install  
  
CMD [ "npm", "start" ]

