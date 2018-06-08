  
FROM node  
  
COPY proxytest /usr/src/app  
RUN cd /usr/src/app; npm install --production  
  
EXPOSE 3000  
CMD ["node", "/usr/src/app/index.js"]  

