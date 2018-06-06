FROM node:7.5  
# Create app directory  
RUN mkdir -p /srv/hdc_web_api/  
WORKDIR /srv/hdc_web_api/  
  
# Install app dependencies  
COPY package.json /srv/hdc_web_api/  
RUN npm install  
  
# Bundle app source  
COPY . /srv/hdc_web_api/  
  
EXPOSE 50001  
CMD [ "node", "server.js"]

