FROM node:6.9-slim  
  
EXPOSE 8080  
RUN npm install restify && npm install mongojs  
  
COPY app.js /  
CMD ["/usr/local/bin/node", "app.js"]  

