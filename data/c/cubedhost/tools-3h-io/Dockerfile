FROM cubedhost/nginx-php-fpm-nodejs:v1.0.8  
ADD .docker/nginx.conf /etc/nginx/conf.d/default.conf  
  
RUN mkdir -p /data/sites/tools.3h.io  
WORKDIR /data/sites/tools.3h.io  
  
ADD . .  
  
RUN curl -Lo /tmp/composer.phar
https://getcomposer.org/download/1.4.2/composer.phar && \  
chmod 755 /tmp/composer.phar  
  
RUN git submodule update --init --force --recursive && \  
cd pma/ && /tmp/composer.phar install  
  
CMD ["/bin/bash", "/start.sh"]  

