# Modified from https://hub.docker.com/r/petronetto/php-nginx-
alpine/~/dockerfile/  
# by Juliano Petronetto <juliano@petronetto.com.br>  
FROM alpine:3.6  
MAINTAINER Rom Luengwattanapong <s1567783@ed.ac.uk>  
  
# Install packages  
RUN apk --update add --no-cache \  
bash \  
coreutils \  
curl \  
docker \  
git \  
nginx \  
php7 \  
php7-bcmath \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-fileinfo \  
php7-fpm \  
php7-gd \  
php7-json \  
php7-mbstring \  
php7-mbstring \  
php7-mcrypt \  
php7-opcache \  
php7-openssl \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-phar \  
php7-session \  
php7-simplexml \  
php7-tokenizer \  
php7-xml \  
php7-zip \  
php7-zlib \  
python3 \  
shadow \  
supervisor \  
tzdata \  
&& rm -rf /var/cache/apk/*  
  
# Configuring timezones  
RUN cp /usr/share/zoneinfo/Europe/London /etc/localtime \  
&& echo "Europe/London" > /etc/timezone \  
&& apk del tzdata && rm -rf /var/cache/apk/*  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# Configure Nginx  
COPY config/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY config/nginx/default /etc/nginx/sites-enabled/default  
  
# Configure PHP-FPM  
COPY config/php/php.ini /etc/php7/php.ini  
COPY config/php/www.conf /etc/php7/php-fpm.d/www.conf  
  
# Configure supervisord  
COPY config/supervisord.conf /etc/supervisord.conf  
  
# Create application folder  
RUN mkdir -p /app  
  
# Setting the workdir  
WORKDIR /app  
  
# Set UID for www user to 1000  
RUN addgroup -g 1000 -S www \  
&& adduser -u 1000 -D -S -G www -h /app -g www www \  
&& chown -R www:www /var/lib/nginx \  
&& chown -R www:www /var/tmp/nginx  
  
# Supervisord  
ADD config/start.sh /start.sh  
RUN chmod +x /start.sh  
  
VOLUME ["/app", "/var/run/docker.sock"]  
EXPOSE 80 443  
# Start Supervisord  
CMD ["/start.sh"]  

