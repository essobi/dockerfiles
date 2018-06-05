# Install the latest node 0.x  
# https://registry.hub.docker.com/_/node/  
FROM node:0  
MAINTAINER Pierre Prinetti  
  
# Copy the node app to the container  
COPY . /src  
  
# Install app dependencies  
RUN cd /src; npm install --production  
  
# Set environment variables  
ENV ACC_MONGODB_DATABASE=acc_prod ACC_MONGODB_USER=acc ACC_MONGODB_HOST=mongo  
  
# Expose the corresponding port  
EXPOSE 80  
# ..and run the application  
CMD ["node", "/src/index.js"]  

