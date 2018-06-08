FROM node:slim  
  
RUN npm update  
RUN npm install -g solid-server  
  
RUN mkdir /solid  
WORKDIR /solid  
  
CMD ["/usr/local/bin/solid", "start"]  

