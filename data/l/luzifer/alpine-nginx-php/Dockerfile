FROM quay.io/luzifer/base-alpine:3.3-1.17.2.0  
# Install packages  
RUN apk-install nginx \  
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
php-mysqli \  
php-pdo_mysql \  
php-phar \  
php-openssl && \  
rm -Rf /var/www/*  
  
# Copy configuration files to root  
COPY rootfs /  
  
# Fix permissions  
RUN chown -Rf nginx:www-data /var/www/  
# Set working directory  
WORKDIR /var/www  
  
# Expose the ports for nginx  
EXPOSE 80 443  

