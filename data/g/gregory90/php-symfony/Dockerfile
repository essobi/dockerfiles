FROM gregory90/php:5.6  
  
RUN mkdir -p /data/app/cache && mkdir -p /data/app/logs && \  
chown -R www-data:www-data /data/app  
  
ADD web/app.php /code/web/app.php  
ADD default /etc/nginx/sites-available/default  
ADD default /etc/nginx/sites-enabled/default  
  

