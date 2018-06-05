FROM alpine:3.4  
MAINTAINER Amrit G.C. <music.demand01@gmail.com>  
  
RUN apk --update add --no-cache --update \  
nginx \  
curl \  
php5-cli \  
php5-common \  
php5-fpm \  
php5-phar \  
php5-pdo \  
php5-json \  
php5-openssl \  
php5-mysql \  
php5-pdo_mysql \  
php5-mcrypt \  
php5-opcache \  
php5-sqlite3 \  
php5-pdo_sqlite \  
php5-ctype \  
php5-zlib \  
php5-curl \  
php5-gd \  
php5-xml \  
php5-dom \  
supervisor \  
xvfb \  
ttf-freefont \  
fontconfig \  
dbus \  
qt5-qtbase-dev; \  
apk add --no-cache \  
\--update \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/community/ \  
\--allow-untrusted \  
php5-xdebug; \  
apk add --no-cache \  
\--update \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \  
\--allow-untrusted \  
wkhtmltopdf \  
php5-memcached;  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer; \  
chmod +x /usr/local/bin/composer;  
  
RUN rm /etc/nginx/nginx.conf  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
ADD conf/default.conf /etc/nginx/default.d/default.conf  
  
ADD conf/nginx-supervisor.ini /etc/supervisor/conf.d/nginx-supervisor.ini  
  
RUN rm -rf /var/cache/apk/*  
  
WORKDIR /app  
COPY conf/zzz-custom.ini /etc/php5/conf.d/  
EXPOSE 80  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/nginx-
supervisor.ini"]  

