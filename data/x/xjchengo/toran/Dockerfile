FROM php:apache  
MAINTAINER xjchengo  
  
COPY toran-proxy-v1.1.7.tgz /var/www/toran-proxy-v1.1.7.tgz  
COPY sources.list /etc/apt/sources.list  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY init.sh /root/init.sh  
  
# Install Utils  
RUN apt-get update && apt-get install -y \  
cron \  
curl \  
vim  
  
RUN sed -i "s/DocumentRoot \/var\/www\/html/DocumentRoot
\/var\/www\/toran\/web/" /etc/apache2/apache2.conf  
RUN cd /var/www && tar -zxf toran-proxy-v1.1.7.tgz  
COPY crontab /var/www/toran/crontab  
RUN rm -rf /var/www/html  
  
WORKDIR /var/www/toran  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

