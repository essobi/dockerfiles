FROM node:4.2.6  
MAINTAINER Ricardo Sanchez Gregorio me@richnologies.io  
  
RUN npm install -g pm2  
  
# A volume is created to store the source code  
VOLUME ["/app"]  
  
# We add the file and allow the container to execute it  
# This command gets execute every time a container is created  
# from this image  
ADD start /start  
RUN chmod 755 /start  
CMD ["/start"]  
  
EXPOSE 1337  

