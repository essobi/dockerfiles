FROM node:alpine  
  
# Create app directory  
WORKDIR /app  
  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
COPY package*.json ./  
  
# Install app dependencies  
ENV NPM_CONFIG_LOGLEVEL warn  
RUN npm install --production  
  
# Bundle app source  
COPY . .  
  
ENV NODE_ENV=production \  
PORT=8080 \  
HOST=http://192.168.8.1 \  
USERNAME=admin \  
PASSWORD=admin \  
PORT=8080  
  
# Show current folder structure in logs  
RUN ls -la  
  
CMD [ "node", "src/index.js" ]  
EXPOSE 8080  
  
USER node  

