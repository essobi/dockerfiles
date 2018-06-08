FROM node:boron-alpine  
  
MAINTAINER Nigel Earle 'nigel@earle.io'  
ENV PORT=5000  
ADD ./app.js /app/  
ADD ./package.json /app/  
  
RUN cd app && npm install  
  
WORKDIR /app  
  
CMD ["npm", "start"]

