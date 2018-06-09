FROM nodesource/jessie:6  
ADD package.json package.json  
RUN npm install  
  
ADD server.js server.js  
  
EXPOSE 80  
CMD ["npm", "start"]

