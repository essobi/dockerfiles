FROM node:latest  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install --silent  
COPY . /usr/src/app  
EXPOSE 9000  
ENV PORT 9000  
CMD [ "npm", "start" ]  
  

