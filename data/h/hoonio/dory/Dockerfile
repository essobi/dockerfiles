FROM node:latest  
MAINTAINER Hoonio  
  
# Bundle app source  
COPY . app/  
WORKDIR app/  
  
# Install app dependencies  
RUN npm install  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

