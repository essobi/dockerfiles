FROM node:argon-slim  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
# Add our user and group first to make sure their IDs get assigned
consistently  
RUN groupadd -r app && useradd -r -g app app  
  
# Set as default user  
USER app  
  
EXPOSE 8080  
CMD [ "node", "index.js" ]  
  

