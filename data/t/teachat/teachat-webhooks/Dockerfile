FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/src/teachat-mailchimp-integration  
WORKDIR /usr/src/teachat-mailchimp-integration  
  
# Install app dependencies  
COPY . /usr/src/teachat-mailchimp-integration  
  
RUN npm install  
  
CMD [ "npm", "start" ]

