FROM node:boron  
  
MAINTAINER "Karl-Heinz Oberkoxholt"  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential make python  
RUN npm install pm2@latest -g  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
  
# Make it the working directory  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY ./package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
# Command to run, if no command is defined in the compose file or if the image
is used by itself.  
CMD [ "pm2-docker", "src/index.js" ]

