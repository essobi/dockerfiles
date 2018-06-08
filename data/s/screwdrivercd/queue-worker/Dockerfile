FROM node:8  
# Screwdriver Queue Worker Version  
ARG VERSION=latest  
  
# Create our application directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install Screwdriver Queue Worker  
RUN npm install screwdriver-queue-worker@$VERSION  
WORKDIR /usr/src/app/node_modules/screwdriver-queue-worker  
  
# Run the service  
CMD [ "npm", "start" ]  

