FROM node:7.6  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Temporary fix for https://github.com/nodejs/docker-node/issues/346  
RUN yarn global add node-gyp  
  
# Install app dependencies (also remove node_modules to prevent leaking host
deps when using with compose)  
COPY package.json yarn.lock ./  
RUN rm -rf node_modules && \  
yarn  
  
# Bundle app source  
COPY . .  
  
# Start server  
CMD [ "npm", "start" ]

