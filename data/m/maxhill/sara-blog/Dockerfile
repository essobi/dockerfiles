FROM node:latest  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
RUN npm install -g pm2  
COPY package.json /usr/src/app/  
RUN yarn install  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 3000  
CMD [ "npm", "run", "prod" ]  

