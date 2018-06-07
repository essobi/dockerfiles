FROM node:6  
# Startup scripts  
ADD . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN npm install -g forever  
RUN npm install  
  
CMD ["forever", "server.js"]  

