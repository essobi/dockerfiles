FROM goffyara/php:7.1-fpm  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -yq \  
&& apt-get install -yq --no-install-recommends \  
nginx \  
supervisor \  
&& apt-get autoremove \  
&& apt-get autoclean \  
&& rm -Rf /etc/nginx/sites-enabled \  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
ADD supervisor /etc/supervisor/  
ADD nginx/config /etc/nginx/conf.d/nginx.conf  
ADD nginx/index.php /var/www/index.php  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]

