FROM alpine:3.7  
LABEL maintainer="Daniel Resnitzky <dresnitzky@luxfacta.com>"  
  
ENV \  
# When using Composer, disable the warning about running commands as
root/super user  
COMPOSER_ALLOW_SUPERUSER=1 \  
# Persistent runtime dependencies  
DEPS="nginx \  
nginx-mod-http-headers-more \  
php7.2 \  
php7.2-phar \  
php7.2-bcmath \  
php7.2-calendar \  
php7.2-mbstring \  
php7.2-exif \  
php7.2-ftp \  
php7.2-openssl \  
php7.2-zip \  
php7.2-sysvsem \  
php7.2-sysvshm \  
php7.2-sysvmsg \  
php7.2-shmop \  
php7.2-sockets \  
php7.2-zlib \  
php7.2-bz2 \  
php7.2-curl \  
php7.2-simplexml \  
php7.2-xml \  
php7.2-opcache \  
php7.2-dom \  
php7.2-xmlreader \  
php7.2-xmlwriter \  
php7.2-tokenizer \  
php7.2-ctype \  
php7.2-session \  
php7.2-fileinfo \  
php7.2-iconv \  
php7.2-json \  
php7.2-posix \  
php7.2-fpm \  
curl \  
ca-certificates \  
runit"  
# PHP.earth Alpine repository for better developer experience  
ADD https://repos.php.earth/alpine/phpearth.rsa.pub
/etc/apk/keys/phpearth.rsa.pub  
  
RUN set -x \  
&& echo "https://repos.php.earth/alpine/v3.7" >> /etc/apk/repositories \  
&& apk add --no-cache $DEPS \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY tags/nginx /  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN rm -f /etc/php/php-fpm.d/*.conf  
COPY ./php-fpm.conf /etc/php/php-fpm.d/www.conf  
  
RUN rm -f /etc/ninx/conf.d/*.conf  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY ./sites/default.conf /etc/nginx/conf.d/default.conf  
RUN chown nginx:www-data -R /var/www/  
  
CMD ["/sbin/runit-wrapper"]  
  

