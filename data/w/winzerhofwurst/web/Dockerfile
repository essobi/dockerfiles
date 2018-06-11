FROM node:10.4.0 as js-builder  
RUN pwd  
COPY . /app  
WORKDIR /app  
RUN npm install  
RUN ./node_modules/webpack-cli/bin/webpack.js --config webpack.prod.config.js
--mode production  
  
FROM composer:latest as php-builder  
COPY . /app  
RUN composer install --no-dev -o  
  
FROM winzerhofwurst/webserver:latest  
COPY . /var/www  
COPY \--from=js-builder /app/public/assets /var/www/public/assets  
COPY \--from=php-builder /app/vendor /var/www/vendor  
RUN chmod -R o+rw /var/www/storage  
WORKDIR /var/www  

