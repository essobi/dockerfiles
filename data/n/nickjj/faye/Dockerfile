# Use the barebones version of Node 0.12.  
FROM node:0.12-slim  
MAINTAINER Nick Janetakis <nick.janetakis@gmail.com>  
  
# Setup the install path for this service.  
ENV INSTALL_PATH /usr/src/service  
RUN mkdir -p $INSTALL_PATH  
  
# Update the workdir to be where our app is installed.  
WORKDIR $INSTALL_PATH  
  
# Ensure bundled packaged are cached and only get updated when necessary.  
COPY package.json package.json  
RUN npm install  
  
# Copy the source from the build machine to the image at the WORKDIR path.  
COPY . .  
  
# The default command to run if no command is specified.  
CMD npm start  

