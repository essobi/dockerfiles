FROM node:6  
# Create directory for app  
RUN mkdir -p /oak-react  
WORKDIR /oak-react  
  
# Install dependencies  
ADD package.json /oak-react  
RUN npm install  
  
# Add rest of app  
ADD . /oak-react  
  
# Expose port  
EXPOSE 8080  
# Start server.js by default  
CMD ["npm", "start"]  
  

