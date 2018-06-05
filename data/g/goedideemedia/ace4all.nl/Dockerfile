FROM node:carbon  
  
# Create app directory  
WORKDIR /usr/src/app  
  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
COPY package*.json ./  
  
# Install app dependencies  
RUN npm install --only=production  
  
# Install the pm2-docker programm  
RUN npm install pm2 -g  
  
# Bundle app source  
COPY . .  
  
# Create our frontend build  
RUN npm run build  
  
# Expose the port node listens to  
EXPOSE 3000  
# Remove some build files  
RUN rm -rf webpack.config.js frontend.js package*.json  
  
# Start the app  
CMD [ "pm2-docker", "--optimize_for_size", "--max_old_space_size", "460", "--
gc_interval", "100", "ecosystem.json" ]  

