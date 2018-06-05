FROM node:5  
# App  
ADD . /  
  
# Install app dependencies  
RUN npm install  
  
# Build app dist files  
RUN npm run build  
  
# Expose port 9000  
EXPOSE 9000  
# Init Server  
CMD npm run serve

