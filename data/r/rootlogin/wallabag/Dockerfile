FROM alpine:latest  
MAINTAINER Simon Erhardt <hello@rootlogin.ch>  
  
ENV WALLABAG_VERSION=2.2.2 \  
SYMFONY__ENV__DATABASE_DRIVER=pdo_sqlite \  
SYMFONY__ENV__DATABASE_HOST=127.0.0.1 \  
SYMFONY__ENV__DATABASE_PORT=~ \  
SYMFONY__ENV__DATABASE_NAME=symfony \  
SYMFONY__ENV__DATABASE_USER=root \  
SYMFONY__ENV__DATABASE_PASSWORD=~ \  
SYMFONY__ENV__MAILER_HOST=127.0.0.1 \  
SYMFONY__ENV__MAILER_USER=~ \  
SYMFONY__ENV__MAILER_PASSWORD=~ \  
SYMFONY__ENV__FROM_EMAIL=wallabag@example.com \  
INSTALL=1  
RUN apk add --update \  
bash \  
curl \  
git \  
nginx \  
openssl \  
php5 \  
php5-bcmath \  
php5-ctype \  
php5-curl \  
php5-dom \  
php5-fpm \  
php5-gd \  
php5-iconv \  
php5-json \  
php5-openssl \  
php5-pdo_mysql \  
php5-pdo_sqlite \  
php5-phar \  
php5-xml \  
supervisor \  
&& rm -rf /var/cache/apk/*  
  
#RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
# && ln -sf /dev/stderr /var/log/nginx/error.log  
COPY etc/supervisord.conf /etc/supervisord.conf  
COPY etc/php-fpm.conf /etc/php5/php-fpm.conf  
COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY etc/nginx/fastcgi_params /etc/nginx/fastcgi_params  
  
RUN mkdir -p /opt/wallabag \  
&& mkdir /opt/wallabag/data \  
&& mkdir /opt/wallabag/bin  
  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN mkdir -p /opt/wallabag/app \  
&& git clone \--branch $WALLABAG_VERSION \--depth 1
https://github.com/wallabag/wallabag.git /opt/wallabag/app  
  
RUN cd /opt/wallabag/app \  
&& SYMFONY_ENV=prod composer install --no-scripts --no-dev -o --prefer-dist  
  
RUN rm -rf /opt/wallabag/app/var/cache/* \  
&& touch /opt/wallabag/app/var/bootstrap.php.cache  
  
COPY bin/* /opt/wallabag/bin/  
  
RUN chmod +x /opt/wallabag/bin/*.sh  
  
EXPOSE 80  
ENTRYPOINT ["/opt/wallabag/bin/run.sh"]  

