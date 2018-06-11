  
# Set the base image  
FROM node:6.11.0-alpine  
  
# Speed up the build process by making use of docker cache:  
# Copy package.json and run npm install first to cache node_modules  
RUN mkdir -p /webapp  
COPY package.json /webapp  
WORKDIR /webapp  
  
# Install and rebuild sass for the current environment  
RUN npm run install:prod  
  
# Copy the app  
ADD . /webapp  
  
# Run production build and clean up afterwards  
RUN npm run full:build:test \  
&& npm remove typescript \  
&& npm cache clean  
  
EXPOSE 8000  
EXPOSE 9000  
# Define commands to be run after deployment  
CMD [ "npm", "--no-color", "run", "start:server"]

