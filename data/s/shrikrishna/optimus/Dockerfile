# Version 0.1.1  
FROM node  
MAINTAINER Shrikrishna Holla  
  
COPY package.json /  
RUN npm install  
COPY . /home/optimus  
WORKDIR /home/optimus  
  
CMD ["/usr/local/bin/npm", "start"]  

