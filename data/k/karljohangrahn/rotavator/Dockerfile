FROM node:6  
# Create directory to hold the application code  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
RUN npm run postinstall  
  
# App runs on this port by default  
EXPOSE 8080  
CMD [ "npm", "start" ]

