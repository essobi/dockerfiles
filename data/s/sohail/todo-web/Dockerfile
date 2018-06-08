FROM node:6.11.0-alpine  
MAINTAINER Sohail Ahmed  
  
# Cache NPM Install  
RUN mkdir -p /app  
ADD package.json /app  
WORKDIR /app  
RUN npm install  
  
# Add Repository & Build  
ADD . /app/  
  
# Expose Ports & Run Application  
EXPOSE 80  
CMD npm start  

