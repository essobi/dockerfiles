FROM wow73611/nginx  
MAINTAINER wow73611 <wow73611@gmail.com>  
  
RUN \  
apt-get update && \  
apt-get install -y supervisor php5 php5-fpm php5-cli && \  
apt-get install -y php5-curl php5-json php-pear php5-mcrypt && \  
apt-get install -y php5-intl php5-dev php5-xdebug && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer  
  
#RUN apt-get install -y php5-sqlite php5-pgsql php5-mysql php5-redis  
  
RUN \  
mkdir -p /var/www/html && \  
echo "<?php phpinfo(); ?>" > /var/www/html/index.php && \  
chown -R www-data:www-data /var/www/html && \  
rm -rf /etc/php5/cli/php.ini && \  
ln -s /etc/php5/fpm/php.ini /etc/php5/cli/php.ini  
  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  
ADD nginx/mysite.conf /etc/nginx/sites-enabled/default  
ADD fpm/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ADD fpm/www.conf /etc/php5/fpm/pool.d/www.conf  
#RUN sed -i '/daemonize /c daemonize = no' /etc/php5/fpm/php-fpm.conf  
  
WORKDIR /var/www/html  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 80  
  
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

