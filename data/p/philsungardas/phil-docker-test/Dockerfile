FROM node:4  
EXPOSE 1337  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
RUN npm --no-color install --silent  
  
CMD [ "npm", "start" ]  

