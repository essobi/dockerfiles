FROM node:alpine  
MAINTAINER Vimalraj Selvam <email2vimalraj@gmail.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apk add --no-cache git  
RUN git clone https://gist.github.com/3c4f35a41c58a55a0ffd00c3e64142c8.git
tmpChange  
RUN git clone https://github.com/anshooarora/extentx.git  
  
RUN mv tmpChange/connections.js extentx/config/connections.js  
RUN rm -rf tmpChange  
  
WORKDIR /usr/src/app/extentx  
  
EXPOSE 1337  
RUN npm install  
  
CMD ["./node_modules/.bin/sails", "lift"]

