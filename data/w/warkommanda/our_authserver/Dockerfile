FROM node:latest  
  
# Create app directory  
WORKDIR /usr/src  
  
# Initiate Server  
RUN npm install -g express-generator@4  
RUN express server  
WORKDIR /usr/src/server  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY /files/ /usr/src/server  
  
# update dependencies  
RUN npm i -g npm-check-updates  
RUN npm-check-updates -u  
  
RUN npm install  
# If you are building your code for production  
# RUN npm install --only=production  
# Bundle app source  
#COPY . .  
  
EXPOSE 3000  
CMD [ "npm", "start" ]  

