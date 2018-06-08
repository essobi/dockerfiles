FROM node:7  
# Create app directory  
RUN mkdir -p /usr/src/chat-app  
WORKDIR /usr/src/chat-app  
  
# Install app dependencies  
COPY package.json /usr/src/chat-app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/chat-app  
  
EXPOSE 8080  
CMD [ "npm", "start" ]

