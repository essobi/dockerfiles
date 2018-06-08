# A docker image for the funktion nodejs runtime container.  
FROM node:7.4.0-onbuild  
RUN npm install -g nodemon  
  
ADD server.js /usr/src/app/server.js  
  
EXPOSE 8888  

