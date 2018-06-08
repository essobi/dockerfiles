FROM node:boron  
  
# Create app directory  
WORKDIR /usr/app  
  
# Install app dependencies  
COPY . .  
  
RUN npm install  
  
# Expose Ports  
EXPOSE 10011  
VOLUME /usr/app/logs  
  
# Run Command  
CMD [ "node", "service.js" ]  

