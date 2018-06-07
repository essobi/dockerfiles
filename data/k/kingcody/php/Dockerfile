FROM php:fpm  
MAINTAINER Cody Mize <docker@codymize.com>  
  
# Add nginx mainline repo  
RUN curl -sSL http://nginx.org/keys/nginx_signing.key | apt-key add - && \  
echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
# Versions  
ENV NGINX_VERSION=1.9.5-1~jessie \  
DOCKERIZE_VERSION=0.0.2  
# Set env defaults  
ENV MAX_UPLOAD=100M  
ENV MAX_EXECUTION_TIME=60  
ENV MAX_INPUT_TIME=60  
RUN apt-get update && \  
apt-get install -y \  
nginx=${NGINX_VERSION} \  
supervisor \  
zip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/{??,??_*}  
  
# Install composer and dockerize  
RUN curl -sSL https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
curl -sSL
"https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-
linux-amd64-v${DOCKERIZE_VERSION}.tar.gz" | \  
tar -xzC /usr/local/bin  
  
# Setup nginx config  
RUN sed -r -e 's/^(\s*)(user) .*$/\1\2 www-data;/' \  
-e 's/^(\s*)(worker_processes) .*$/\1\2 {{ .Env.NGINX_WORKERS }};/' \  
-e 's/^(\s*)(keepalive_timeout) .*$/\1\2 2;/' \  
-e 's/^(\s*)(keepalive_timeout .*)$/\1\2\n\1client_max_body_size {{ .Env.MAX_UPLOAD }};/' \  
-i /etc/nginx/nginx.conf  
  
# Setup php config  
COPY php.ini /usr/local/etc/php/  
COPY php-fpm.conf /usr/local/etc/  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
ln -sf /dev/stdout /var/log/php5-fpm.log  
  
VOLUME ["/var/cache/nginx"]  
  
# Setup default site  
COPY nginx-site.conf /etc/nginx/conf.d/default.conf  
RUN echo '<?php phpinfo(); ?>' > /var/www/html/index.php && \  
chown -Rf www-data:www-data /var/www/html/  
  
# Supervisor Config  
COPY supervisor /etc/supervisor  
  
# Entrypoint with dockerize  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Expose Ports  
EXPOSE 80 443  
# Set supervisord as the default cmd  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

