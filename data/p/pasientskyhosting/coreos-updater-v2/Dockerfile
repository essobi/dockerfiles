FROM pasientskyhosting/nginx-nodejs  
  
WORKDIR /var/www/html/  
  
ADD package.json server.js config.json /var/www/html/  
COPY src /var/www/html/src  
  
VOLUME ["/var/www/html/coreos"]  
  
RUN npm install  

