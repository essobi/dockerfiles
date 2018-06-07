# Get node from source TODO: get spectifc verstion of node  
FROM node  
  
# Labels for the image  
LABEL organization="INWK-DAL"  
LABEL maintainer="Tito"  
LABEL description="React Application for VIRL"  
  
# The base node image sets a very verbose log level.  
ENV NPM_CONFIG_LOGLEVEL warn  
  
  
# Change working directory  
WORKDIR /inwk-labs  
  
# Copy all local files into the image.  
COPY . /inwk-labs  
  
# Install Stuff.  
RUN npm install  
  
# To take care of node-sass enviroment error  
RUN npm rebuild node-sass  
  
# Build for production.  
RUN npm run build --production  
  
# Install `serve` to run the application.  
RUN npm install -g serve  
  
# Set the command to start the node server.  
CMD serve -s build  
  

