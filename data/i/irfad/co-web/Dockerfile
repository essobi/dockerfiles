# docker build -t co-web .  
# docker stop co-web && docker rm co-web  
# docker run -d --name co-web --network=host -e DB_HOST=127.0.0.1 -e
DB_NAME=crossover -e DB_USER=crossover -e DB_PASSWORD=secret-co co-web  
# docker exec -ti co-web /bin/bash  
from php:5.6-apache  
  
maintainer Irfad Razick  
  
RUN docker-php-ext-install mysql pdo_mysql  
  
ADD src/.htpasswd /var/www/.htpasswd  
ADD src/.htaccess /var/www/html/.htaccess  
  
ADD src/db.php /var/www/html/db.php  
ADD src/index.html /var/www/html/index.html  

