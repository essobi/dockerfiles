FROM ubuntu  
  
RUN apt-get update -y && \  
apt-get install -y \  
php-fpm php-mysql  
  
VOLUME ["/var/www/html"]  
WORKDIR /var/www/html  
EXPOSE 9000  
CMD ["php7-fpm.0"]  
  
#docker run -p 8080:9000 -d -v $(pwd):/var/www/html test/php php -S
0.0.0.0:9000

