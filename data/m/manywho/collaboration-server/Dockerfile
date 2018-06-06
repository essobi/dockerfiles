FROM mhart/alpine-node  
  
EXPOSE 4444  
ENTRYPOINT ["node", "server.js"]  
  
WORKDIR /src  
COPY package.json .  
  
RUN npm install --production  
  
COPY server.js .  

