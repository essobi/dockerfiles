#  
# ISY994i device server for integration with the SmartThings Hub  
#  
# http://github.com/tenstartups/smartthings-isy-bridge  
#  
FROM node:alpine  
  
# Install base packages.  
RUN \  
apk --update add \  
git \  
rm -rf /var/cache/apk/*  
  
# Create app directory.  
WORKDIR /usr/src/app  
  
# Install app dependencies.  
COPY Gruntfile.js .  
COPY package.json .  
  
# Install node application.  
RUN npm install  
  
# Install app source  
ADD tasks tasks  
ADD config config  
ADD assets assets  
ADD api api  
COPY app.js .  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

