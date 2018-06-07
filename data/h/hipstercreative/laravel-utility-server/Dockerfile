FROM php:7.2.1-fpm-alpine3.7  
RUN apk update \  
&& apk add --no-cache openssh-client git nginx supervisor bash mysql mysql-
client vim \  
gd freetype libpng libjpeg-turbo freetype-dev libpng-dev libjpeg-turbo-dev
php7-zip \  
&& apk add gnu-libiconv --update-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install pdo_mysql  
  
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php  
  
ADD https://getcomposer.org/composer.phar /usr/bin/composer  
  
RUN chmod 0755 /usr/bin/composer \  
&& mkdir -p /run/nginx \  
&& touch /run/nginx/nginx.pid \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& rm -fr /www && mkdir /www \  
&& mkdir -p /var/log/supervisor \  
&& mkdir -p /var/log/nginx/ \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
ADD ./etc/nginx/conf.d/default.conf /etc/nginx/conf.d/  
ADD ./etc/nginx/snippets/cors-wildcard.conf /etc/nginx/snippets/  
  
ADD ./etc/mysql/my.cnf /etc/mysql/  
  
# Set up cron  
ADD ./var/spool/cron/crontabs/www-data /var/spool/cron/crontabs/  
RUN chmod 0600 /var/spool/cron/crontabs/www-data  
  
# Configure supervisord  
ADD ./etc/supervisor/supervisord.conf /etc/supervisor/  
ADD ./etc/supervisor/conf.d/* /etc/supervisor/conf.d/  
  
COPY ./root/_ssh /root/.ssh  
COPY ./root/docker-entrypoint.sh /root/docker-entrypoint.sh  
ADD ./root/scripts /root/scripts  
  
VOLUME /www  
VOLUME /mysql  
EXPOSE 8080  
EXPOSE 3306  
ENTRYPOINT ["/root/docker-entrypoint.sh"]  

