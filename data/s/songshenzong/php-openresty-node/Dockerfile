# Dockerfile - php-openresty-node  
FROM songshenzong/php-openresty  
  
RUN apk add --no-cache \  
nodejs \  
nodejs-npm \  
&& npm install laravel-echo-server -g  
  
EXPOSE 443 80 9000 6001  

