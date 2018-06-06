#reusable docker image for node projects - taken from nodejs.org  
#latest LTS version of node available from Docker Hub  
FROM node:carbon  
  
# Create app directory - holds the code  
WORKDIR /usr/src/app  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY package*.json ./  
  
# building code  
RUN npm install  
  
# Bundle app source  
COPY . .  
  
EXPOSE 3000  
#adjusted run script for docker  
CMD [ "npm", "run", "docker" ]

