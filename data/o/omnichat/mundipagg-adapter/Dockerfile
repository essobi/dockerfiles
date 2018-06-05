#FROM node:4.4.3  
FROM mhart/alpine-node:base-6.9.1  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 5000  
CMD [ "node", "./built/src/server.js" ]

