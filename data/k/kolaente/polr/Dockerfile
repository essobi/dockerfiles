FROM alpine:3.5  
MAINTAINER kolaente - mowie.cc  
  
ENV TZ "Europe/Berlin"  
# Install NGINX and PHP 7  
RUN apk update && \  
apk --no-cache add bash tzdata curl ca-certificates s6 ssmtp mysql-client \  
nginx nginx-mod-http-headers-more && \  
ln -sf "/usr/share/zoneinfo/$TZ" /etc/localtime && \  
echo "$TZ" > /etc/timezone && date && \  
apk --no-cache add \  
php7 php7-phar php7-curl php7-fpm php7-json php7-zlib php7-gd \  
php7-xml php7-dom php7-ctype php7-opcache php7-zip php7-iconv \  
php7-pdo php7-pdo_mysql php7-mysqli php7-mbstring php7-session \  
php7-mcrypt php7-openssl php7-sockets php7-posix php7-mbstring php7-gettext &&
\  
rm -rf /var/cache/apk/* && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
rm -f /etc/php7/php-fpm.d/www.conf && \  
touch /etc/php7/php-fpm.d/env.conf && \  
rm -rf /var/www  
  
# Copy Config  
COPY conf/services.d /etc/services.d  
COPY conf/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY conf/php/php-fpm.conf /etc/php7/  
COPY conf/php/conf.d/php.ini /etc/php7/conf.d/zphp.ini  
  
# Copy Polr  
COPY polr-2.2.0 /var/www  
  
#Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Polr dependencies  
RUN cd /var/www && \  
php /usr/local/bin/composer install --no-dev -o  
  
# Permissions  
RUN mkdir /var/session && \  
chown -R nginx:nginx /var/www && \  
chown -R nginx:nginx /var/session && \  
chmod 750 /var/www -R  
  
# Add Volumes  
VOLUME /var/session  
  
EXPOSE 80  
ENTRYPOINT ["/bin/s6-svscan", "/etc/services.d"]  
CMD []  

