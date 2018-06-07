FROM richarvey/nginx-php-fpm:latest  
MAINTAINER yaochenfeng <282696845@qq.com>  
  
  
ENV COMPOSER_ALLOW_SUPERUSER=1  
ENV GIT_USERNAME=yaochenfeng  
ENV GIT_EMAIL=282696845@qq.com  
WORKDIR /var/www/html  
VOLUME /app/data/  
  
RUN echo http://mirrors.aliyun.com/alpine/v3.6/main > /etc/apk/repositories;  
  
COPY nginx.vh.default.conf /etc/nginx/sites-available/default.conf  
ADD index.php /var/www/html/public/index.php  
EXPOSE 443 80  
CMD ["/start.sh"]  

