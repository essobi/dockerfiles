FROM node:9  
  
# Set curr dir to app directory  
WORKDIR /usr/src/app/tweetmybot/  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY package*.json ./  
  
RUN npm install  
# If you are building your code for production  
# RUN npm install --only=production  
# Bundle app source  
#COPY /.compiled/* ./  
#copy the contents of the .compiled folder to curr dir  
ADD .compiled ./  
ADD config ./config  
  
EXPOSE 8081  
#CMD node app.js  
ENTRYPOINT ["node", "app.js"]  
  

