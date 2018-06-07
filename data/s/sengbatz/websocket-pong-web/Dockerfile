FROM node:9.3.0  
# Create app directory  
WORKDIR /usr/src/app  
  
COPY sources/public_html/ ./  
  
RUN npm install  
  
HEALTHCHECK \--interval=5s --timeout=3s CMD curl --fail http://localhost:8081
|| exit 1  
  
EXPOSE 8081  
CMD [ "nodejs", "/usr/src/app/server.js" ]  

