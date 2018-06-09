FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/src/teachat-slack-bot  
WORKDIR /usr/src/teachat-slack-bot  
  
# Install app dependencies  
COPY . /usr/src/teachat-slack-bot  
  
RUN npm install  
  
CMD [ "npm", "start" ]

