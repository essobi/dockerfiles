# Begin with Linux distro with only node installed  
FROM node:latest  
  
# I am the wizard who conjured this machine  
MAINTAINER Sam Reaves  
  
# On container start, build app directory  
RUN mkdir /app  
  
# Install global node monitor  
RUN npm install nodemon -g  
  
# Set app directory as default directory for start command  
WORKDIR /app  
  
# Add local current directory to container's app directory  
ADD . /app  
  
# Install dependencies  
RUN npm install  
  
# Open port 3000  
EXPOSE 3000  
# It's business time  
CMD npm start

