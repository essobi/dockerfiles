FROM alpine:latest  
MAINTAINER Tesla <tesla@v-ip.fr>  
COPY migration_sqlite_patch /  
RUN apk add \--update \--virtual git patch && apk add \--no-cache nginx
php5-fpm php5 php5-ctype php5-xml php5-gd php5-zlib php5-bz2 php5-zip
php5-openssl \  
php5-curl php5-opcache php5-json curl php5-phar php5-dom php5-pdo
php5-pdo_sqlite sqlite gettext && \  
mkdir /www && cd /www/ && git clone https://github.com/cydrobolt/polr.git
\--depth=1 && mkdir /run/nginx; adduser www-data -G www-data -S && \  
cd /www/polr/ && patch -p0 < /migration_sqlite_patch && \  
ln -s /usr/bin/php5 /usr/bin/php && \  
ln -s /usr/bin/php-fpm5 /usr/bin/php-fpm && \  
ln -s /etc/php5 /etc/php && \  
curl -sS https://getcomposer.org/installer | php && php composer.phar install
\--no-dev -o && \  
chown -R www-data:www-data /www && chown -R www-data:www-data /var/lib/nginx
&& \  
apk del git && rm -rf /var/lib/apt/lists/* && rm /migration_sqlite_patch  
COPY conf_polr /www/polr/conf_polr  
COPY php-fpm.conf /etc/php/  
COPY nginx.conf /etc/nginx/  
  
COPY run.sh /run.sh  
RUN chmod u+rwx /run.sh  
EXPOSE 80  
  
  
ENTRYPOINT [ "/run.sh" ]  

