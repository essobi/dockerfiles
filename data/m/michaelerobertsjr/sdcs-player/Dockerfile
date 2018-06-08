FROM node:onbuild  
MAINTAINER michael.e.roberts.jr@gmail.com  
  
# Copy app to /src  
COPY . /src  
  
# Install app and dependencies into /src  
RUN cd /src; npm install; gulp bundle  
  
EXPOSE 8080  
CMD ["node", "/src/server/server.js"]  

