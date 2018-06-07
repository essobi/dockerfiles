# specify the node base image with your desired version node:<version>  
FROM node:9.5  
ENV NPM_CONFIG_LOGLEVEL info  
  
# replace this with your application's default port  
EXPOSE 3000  
EXPOSE 80  
# Create app directory  
WORKDIR /  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
ADD package*.json ./  
  
RUN npm install  
  
# Bundle app source  
ADD . .  
  
EXPOSE 8080  
CMD [ "npm", "start" ]

