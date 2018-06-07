FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
# Install stupid-cms-db  
RUN npm install -g stupid-cms-db  
EXPOSE 3000  
CMD stupid-cms --port 3000  
  

