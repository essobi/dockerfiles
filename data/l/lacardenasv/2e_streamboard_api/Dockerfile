FROM node:carbon-slim  
  
# Create app directory  
WORKDIR /git/streamboard_api  
  
# Install app dependencies  
COPY package.json /git/streamboard_api/  
RUN npm install  
  
# Bundle app source  
COPY . /git/streamboard_api/  
RUN npm run prepublish  
  
CMD [ "npm", "run", "runServer" ]  
  
EXPOSE 5000  

