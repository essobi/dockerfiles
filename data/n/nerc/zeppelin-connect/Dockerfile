FROM node:8.2.1-alpine  
  
LABEL maintainer "gareth.lloyd@stfc.ac.uk"  
  
RUN mkdir -p /usr/src/  
  
WORKDIR /usr/src/  
  
COPY ./src/server.js /usr/src/server.js  
  
EXPOSE 8000  
CMD ["node", "server.js"]

