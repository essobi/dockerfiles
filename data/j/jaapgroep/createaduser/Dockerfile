# last version of Alpine-node OS  
FROM mhart/alpine-node:latest  
  
# Ceate app dir  
RUN mkdir -p /user/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app  
RUN npm install  
  
# Bundle your app source code  
COPY . /usr/src/app  
  
# Port binding  
EXPOSE 8080  
# Command to run your app using CMD (using npm start to run the server.js to
start the server)  
CMD [ "npm", "start" ]  

