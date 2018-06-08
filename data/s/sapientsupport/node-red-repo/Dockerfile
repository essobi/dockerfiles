FROM node:6.2  
  
MAINTAINER Amol  
  
# install node-red  
RUN npm install -g node-red  
RUN npm install -g node-red-node-mongodb  
RUN npm install -g node-red-node-email  
RUN npm install -g node-red-contrib-mail-parse  
# expose port  
EXPOSE 1880  
# Set the default command to execute  
# when creating a new container  
CMD ["/usr/local/bin/node-red"]  

