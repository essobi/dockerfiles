# You should always specify a full version here to ensure all of your
developers  
# are running the same version of Node.  
FROM node:7.8.0  
# The base node image sets a very verbose log level.  
ENV NPM_CONFIG_LOGLEVEL warn  
  
# Prepare app directory  
RUN mkdir -p /usr/src/app  
ADD . /usr/src/app  
  
# Install dependencies  
WORKDIR /usr/src/app  
  
RUN npm install  
  
# Build for production.  
RUN npm run build .env.production --production  
  
# Install `serve` to run the application.  
RUN npm install -g serve  
  
# Set the command to start the node server.  
CMD serve -s build  
  
# Tell Docker about the port we'll run on.  
EXPOSE 5000

