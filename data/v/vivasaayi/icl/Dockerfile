FROM vivasaayi/nodejs  
  
WORKDIR .  
  
RUN npm install --verbose  
RUN node /node_modules/.bin/bower install --allow-root --verbose  
  
COPY . /src  
  
CMD ["node", "/src/app.js"]  
  

