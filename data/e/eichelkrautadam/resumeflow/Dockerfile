# You should always specify a full version here to ensure all of your
developers  
# are running the same version of Node.  
FROM node:alpine  
  
# Copy all local files into the image.  
COPY build .  
  
# Build for production.  
#RUN npm run build --production  
# Install `serve` to run the application.  
RUN npm install -g serve  
  
# Set the command to start the node server.  
CMD serve -s --port 80

