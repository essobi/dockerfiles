  
FROM mhart/alpine-node:7.4.0  
WORKDIR /server  
  
COPY ./ ./  
  
RUN npm install --production  
  
EXPOSE 3030  
ENTRYPOINT ["npm", "start"]  

