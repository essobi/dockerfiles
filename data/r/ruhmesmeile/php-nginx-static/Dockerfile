FROM webdevops/php-nginx:ubuntu-16.04  
# Add application dir  
RUN mkdir -p /app/  
WORKDIR /app/  
  
# Configure PHP  
COPY config/php/99-docker.php.ini /etc/php/7.0/fpm/conf.d/99-docker.ini  
  
# Configure PHP FPM  
COPY config/php/application.conf /etc/php/7.0/fpm/pool.d/application.conf  
  
# Configure Nginx  
COPY config/nginx/vhost.conf /opt/docker/etc/nginx/vhost.conf  
COPY config/nginx/09-fpm.conf /opt/docker/etc/nginx/vhost.common.d/09-fpm.conf  
  
# Configure cronjob  
COPY config/cron/cron.conf /opt/docker/etc/supervisor.d/cron.conf  
  
# Install MySQL client  
RUN /usr/local/bin/apt-install mysql-client-5.7 \  
&& docker-image-cleanup  
  
# Add user and fix permissions  
RUN adduser www-data application  

