FROM google/nodejs  
  
COPY . /app  
WORKDIR /app  
  
RUN npm install && npm install -g supervisor  
  
CMD ["supervisor", "app/server/home.js"]  

