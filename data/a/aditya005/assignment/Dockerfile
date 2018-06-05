# Use the node version by searching in docker hub  
FROM node:6.11-slim  
  
# Create app directory  
WORKDIR /usr/src/app  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY package*.json ./  
  
# install dependecies  
RUN npm install  
  
# Bundle app source  
COPY . .  
  
# build app source code  
# COPY . ./  
EXPOSE 80  
# runtime configs  
ENTRYPOINT ["./entrypoint.sh"]  
# CMD ["npm", "start"]  

