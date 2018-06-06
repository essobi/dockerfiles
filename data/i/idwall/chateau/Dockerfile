FROM node:8.4.0-alpine  
  
RUN npm install -g chateau  
COPY config.js /  
  
CMD ["chateau", "-f", "/config.js"]

