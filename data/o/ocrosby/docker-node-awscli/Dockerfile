FROM node:carbon  
  
# Create a working directory  
WORKDIR /usr/src  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY package*.json ./  
  
RUN npm install --only=production  
  
CMD ["npm", "start"]

