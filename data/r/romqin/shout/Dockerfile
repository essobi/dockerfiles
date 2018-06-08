FROM node:latest  
  
MAINTAINER Romain Gautier <mail+dh@romain.sh>  
  
RUN npm install -g shout  
  
VOLUME ["/config"]  
  
EXPOSE 9000  
ENTRYPOINT ["shout", "--home", "/config"]  

