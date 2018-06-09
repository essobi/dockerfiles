# define from what image we want to build from  
FROM node:carbon  
  
# Set the working directory to /app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package*.json ./  
  
RUN npm install  
  
# If you are building your code for production  
# RUN npm install --only=production  
# Bundle app source  
COPY . .  
  
RUN npm run build  
  
# Your app binds to port 8080 so you'll use the EXPOSE instruction to have it
mapped by the docker daemon:  
EXPOSE 5000  
# npm start which will run node server.js to start your server:  
CMD [ "npm", "run", "serve" ]

