FROM node:carbon  
  
# Create app directory  
WORKDIR /usr/src/app  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY package*.json ./  
  
RUN npm install  
# If you are building your code for production  
# RUN npm install --only=production  
# Install PM2  
RUN npm install -g pm2  
  
RUN mkdir -p /var/www/html  
  
# Define working directory  
WORKDIR /var/www/html  
  
ADD . /var/www/html  
COPY . .  
  
#ENTRYPOINT ["pm2","server.js"]  
# Expose port  
EXPOSE 3003  
# Run app  
CMD pm2 start --no-daemon server.js  
#CMD pm2 resurrect --no-daemon server.js  
# Bundle app source  
#ENTRYPOINT ["/usr/local/bin/pm2","start","server.js"]  
#ENTRYPOINT [ "pm2", "start","--no-daemon","processes.json" ]  

