FROM node:8  
  
# Screwdriver Store Version  
ARG VERSION=latest  
  
# Create our application directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install Screwdriver API  
RUN npm install screwdriver-store@$VERSION  
WORKDIR /usr/src/app/node_modules/screwdriver-store  
  
# Setup configuration folder  
RUN ln -s /usr/src/app/node_modules/screwdriver-store/config /config  
  
# Expose the web service port  
EXPOSE 80  
  
# Run the service  
CMD [ "npm", "start" ]  

