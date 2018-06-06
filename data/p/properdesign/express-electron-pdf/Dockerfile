# FROM node:5-slim  
FROM kipparker/docker-tape-run  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Install electron  
RUN npm install electron-pdf -g  
  
# Make output directory. Everything in here will be publicly accessible  
RUN mkdir -p /www  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  
# CMD Xvfb -ac -screen scrn 1280x2000x24 :9.0 & export DISPLAY=:9.0 && npm
start

