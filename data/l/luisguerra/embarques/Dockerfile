FROM node:8.9.3  
# Install Nano  
RUN apt-get update  
RUN apt-get install -y nano  
  
# Folder structure setup  
RUN mkdir /embarques  
COPY . /embarques  
WORKDIR /embarques  
  
# Install dependencies  
RUN npm install  
  
# Build the Angular App  
RUN npm run build  

