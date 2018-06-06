FROM node:7.2.0  
# Create directories  
RUN mkdir -p /usr/src/webfrontend && mkdir -p /usr/src/paenzsystem  
  
# Install server dependencies  
WORKDIR /usr/src/paenzsystem  
COPY Server/package.json /usr/src/paenzsystem/  
RUN npm install  
  
# Setup WebFrontEnd build environment  
WORKDIR /usr/src/webfrontend  
COPY WebFrontEnd/package.json /usr/src/webfrontend/  
RUN npm install  
  
# Copy sources  
COPY Server/ /usr/src/paenzsystem  
COPY WebFrontEnd/ /usr/src/webfrontend  
  
# Make WebFrontEnd  
RUN npm run build-docker && rm -rf /usr/src/webfrontend  
  
# Setup Server  
WORKDIR /usr/src/paenzsystem  
RUN chmod -R +rx /usr/src/paenzsystem  
  
EXPOSE 8080  
EXPOSE 8443  
CMD [ "npm", "start" ]  

