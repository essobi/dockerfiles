FROM readytalk/nodejs  
  
WORKDIR /app  
ADD package.json /app/  
RUN npm install  
ADD . /app  
  
EXPOSE 3000  
CMD ["/nodejs/bin/node", "/app/app.js"]  
#ENTRYPOINT ["/nodejs/bin/npm", "start"]  

