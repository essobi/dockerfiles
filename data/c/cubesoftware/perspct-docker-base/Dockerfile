FROM alpine:3.6  
  
# Install packages (https://www.cyberciti.biz/faq/how-to-install-php-7-fpm-on-
alpine-linux/)  
RUN apk --no-cache add php7 php7-fpm php7-mysqli php7-pdo php7-pdo_mysql
php7-json php7-openssl php7-curl \  
php7-zlib php7-xml php7-phar php7-intl php7-dom php7-xmlreader php7-ctype
php7-simplexml \  
php7-mbstring php7-gd php7-session php7-curl php7-tokenizer php7-opcache nginx
supervisor curl  
  
# Configure nginx  
COPY dockerConfig/nginx.conf /etc/nginx/nginx.conf  
  
# Configure PHP-FPM  
COPY dockerConfig/fpm-pool.conf /etc/php7/php-fpm.d/zzz_custom.conf  
COPY dockerConfig/php.ini /etc/php7/conf.d/zzz_custom.ini  
  
#Configure Opcache  
COPY dockerConfig/opcache.ini /etc/php7/conf.d/opcache.ini  
  
EXPOSE 80  

