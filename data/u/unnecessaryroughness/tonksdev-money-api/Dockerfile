FROM node:4-onbuild  
# Copy app to /src  
COPY . /src  
  
RUN cd /src; npm install  
  
EXPOSE 8081  
CMD cd /src && DEBUG=tonksDEV:* node ./server.js  

