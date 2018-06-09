FROM node:slim  
  
# Create app directory  
WORKDIR /usr/src/app  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY package*.json ./  
RUN mkdir ./public  
COPY public/package*.json ./public  
  
RUN yarn install && \  
cd ./public && \  
yarn install --modules-folder ./lib  
  
# If you are building your code for production  
# RUN npm install --only=production  
# Bundle app source  
COPY . .  
  
EXPOSE 80  
CMD [ "npm", "start" ]  

