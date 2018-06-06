FROM node:argon  
  
# Create app directory  
RUN mkdir -p /srv/hdc_uploader/  
RUN mkdir -p /srv/logs/  
WORKDIR /srv/hdc_uploader/  
  
# Install app dependencies  
COPY package.json /srv/hdc_uploader/  
RUN npm install  
  
# Bundle app source  
COPY . /srv/hdc_uploader/  
  
RUN echo "172.16.238.10 demo.hdcbc.ca" >> /etc/hosts  
RUN echo "172.16.238.10 integration.hdcbc.ca" >> /etc/hosts  
RUN echo "172.16.238.10 staging.hdcbc.ca" >> /etc/hosts  
RUN echo "172.16.238.10 production.hdcbc.ca" >> /etc/hosts  
  
# Run the app  
CMD [ "node", "index.js"]  

