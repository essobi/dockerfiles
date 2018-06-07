FROM node:boron  
MAINTAINER jake@jakebladt.com  
  
WORKDIR /webclient  
COPY . /webclient  
RUN rm /webclient/public/scripts/config.js  
COPY ./public/scripts/config.dev.js /webclient/public/scripts/config.js  
EXPOSE 5665:5665  
RUN npm install  
CMD ["node", "client.js"]  

