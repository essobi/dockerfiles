FROM readytalk/nodejs:latest  
RUN npm install -g bower  
RUN npm install -g gulp  
  
COPY server.js /home/  
  
ENTRYPOINT ["node", "/home/server.js"]

