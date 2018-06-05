FROM node:6  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN npm install; exit 0  
RUN npm install -g bower  
RUN bower install --allow-root  
  
ENV PORT 80  
EXPOSE 80  
CMD ["node", "server.js"]  

