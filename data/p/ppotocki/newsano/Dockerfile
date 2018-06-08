FROM node:9.7  
RUN mkdir -p /usr/src/app/src/  
WORKDIR /usr/src/app  
  
COPY src/. /usr/src/app/src/  
COPY ./ /usr/src/app/  
  
COPY package.json /usr/src/app/  
RUN npm install  
  
EXPOSE 8765  
CMD [ "npm", "start" ]  

