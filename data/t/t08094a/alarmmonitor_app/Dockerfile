# use latest LTS version  
FROM node:carbon  
  
WORKDIR /usr/src/app  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY package*.json ./  
  
RUN npm install  
  
# If you are building your code for production  
#RUN npm install --only=production  
# Bundle app source  
COPY . .  
  
# Use port 8080 for the app  
EXPOSE 8080  
# Run app with 'npm start' which will run 'node server.js'  
CMD ["npm", "start"]  
  
# Run the container as an unprivileged user 'node' wherever possible  
USER node  

