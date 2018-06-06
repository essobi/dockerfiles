FROM alpine:3.6  
# Install packages  
RUN apk --no-cache add php7 php7-fpm php7-cli php7-mysqli php7-json
php7-openssl php7-curl \  
php7-zlib php7-xml php7-phar php7-intl php7-dom php7-xmlreader php7-ctype
php7-pdo \  
php7-mysqli php7-tokenizer php7-mbstring php7-gd php7-session nginx supervisor
curl  
  
# Configure nginx  
COPY docker/nginx.conf /etc/nginx/nginx.conf  
  
# Configure PHP-FPM  
COPY docker/fpm-pool.conf /etc/php7/php-fpm.d/zzz_custom.conf  
COPY docker/php.ini /etc/php7/conf.d/zzz_custom.ini  
  
# Configure supervisord  
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Add application  
RUN mkdir -p /application  
COPY . /application  
WORKDIR /run  
  
# Expose ports and run  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

