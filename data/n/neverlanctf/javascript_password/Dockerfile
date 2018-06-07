FROM richarvey/nginx-php-fpm  
  
MAINTAINER Zane Durkin <zane@zemptech.com>  
  
# set up nginx  
RUN sed -i 's/root \/usr\/share\/nginx\/html/root \/var\/www\/html/g'
/etc/nginx/sites-enabled/default.conf  
RUN rm /var/www/html/*  
  
COPY web /var/www/html  
  
#RUN sed -i 's/try_files $uri $uri\/ \/index.php/try_files $uri $uri\/
\/index.html/g' /etc/nginx/sites-available/default.conf  
#RUN sed -i 's/index index\\.php/index index\\.html index\\.php/g'
/etc/nginx/sites-available/default.conf  
#RUN sed -i 's/fastcgi_index index.html index.php/fastcgi_index index.html/g'
/etc/nginx/sites-available/default.conf  

