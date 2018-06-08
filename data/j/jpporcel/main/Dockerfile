# Start from a standard nodejs image  
FROM node  
MAINTAINER Juan Pablo Porcel Porcel <juanpiporcel@gmail.com>  
EXPOSE 8080  
# Install libraries  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev
libkrb5-dev  
  
# Set working directory  
RUN mkdir /app  
WORKDIR /app  
  
# Install dependencies  
ADD package.json /app/package.json  
RUN npm install  
  
# Add files to the image  
ADD . /app  
  
CMD node main.js  

