FROM takatost/nginx-php-fpm:latest  
  
MAINTAINER JohnWang <wangjiajun@vchangyi.com>  
  
COPY dockerfiles/nginx/default.conf /etc/nginx/sites-available/default.conf  
COPY src /data/www  
COPY dockerfiles/supervisor/queue.conf /etc/supervisor/conf.d/  
COPY dockerfiles/supervisor/chown.conf /etc/supervisor/conf.d/  
  
VOLUME /data/www/storage  
  
RUN cd /data/www && \  
composer install --no-dev -vvv && \  
chown -R nginx:nginx /data/www  
  

