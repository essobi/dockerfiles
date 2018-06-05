FROM richarvey/nginx-php-fpm  
  
MAINTAINER Zane Durkin <zane@zemptech.com>  
  
# set up nginx  
RUN sed -i 's/root \/usr\/share\/nginx\/html/root \/var\/www\/html/g'
/etc/nginx/sites-enabled/default.conf  
RUN rm /var/www/html/*  
  
# import web files  
COPY web/ /var/www/html  

