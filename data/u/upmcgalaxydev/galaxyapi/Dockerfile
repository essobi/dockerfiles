# GalaxyAPI Dockerfile  
# Specify base node.js image  
FROM node:boron  
  
# Create application directory  
RUN mkdir -p /usr/src/galaxyAPI  
  
# Set the current working directory  
WORKDIR /usr/src/galaxyAPI  
  
# Copy source code  
COPY . /usr/src/galaxyAPI/  
  
# Set strict-ssl to false if you see cert issues  
RUN npm config set strict-ssl false  
  
# Install application dependencies  
RUN npm install  
  
# Make port 3000 available to the world outside this container  
EXPOSE 3000  
#Define command to run the application  
CMD [ "npm", "start" ]  

