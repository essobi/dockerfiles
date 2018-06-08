FROM alpine:3.3  
MAINTAINER lw6c@qq.com  
  
RUN apk --no-cache add ca-certificates && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk && \  
apk add glibc-2.25-r0.apk  
  
# Install packages  
RUN apk update && apk add s6 \  
nginx \  
bash \  
curl \  
git \  
php-cli \  
php-curl \  
php-dom \  
php-gd \  
php-fpm \  
php-json \  
php-mcrypt \  
php-mysql \  
php-pdo_mysql \  
php-phar \  
php-iconv \  
php-openssl && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
rm -Rf /var/www/*  
  
# Copy configuration files to root  
COPY rootfs /  
RUN chmod +x /etc/services.d/nginx/* && chmod +x /etc/services.d/php-fpm/* &&
\  
chmod +x /etc/services.d/.s6-svscan/*  
  
RUN adduser -u 1000 -D -S -G www-data www-data  
  
# Fix permissions  
RUN chown -Rf www-data:www-data /var/www/  
  
# Set working directory  
WORKDIR /var/www  
  
# Expose the ports for nginx  
EXPOSE 80 443  
CMD ["s6-svscan", "/etc/services.d"]

