FROM node:8  
MAINTAINER Mobapi "contact@mobapi.com"  
RUN npm install -g pm2@2.10.2  
  
RUN mkdir /app  
VOLUME ["/app"]  
  
CMD ["pm2-docker", "--web", "9615"]  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 9615  

