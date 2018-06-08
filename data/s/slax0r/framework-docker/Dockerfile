FROM debian:testing  
MAINTAINER Tomaz Lovrec <tomaz.lovrec@gmail.com>  
  
# Install packages  
RUN apt-get update  
RUN apt-get install -y \  
php-common \  
php-pear \  
php-xml \  
php7.0-cli \  
php7.0-common \  
php7.0-dev \  
php7.0-fpm \  
php7.0-intl \  
php7.0-json \  
php7.0-mysql \  
php7.0-opcache \  
php7.0-pgsql \  
php7.0-readline \  
php7.0-xml \  
php7.0-curl \  
php7.0-mbstring \  
nginx \  
git  
  
# Create www-user user  
RUN adduser www-user  
  
# Configure web server (nginx)  
RUN rm -f /etc/nginx/sites-available/default  
RUN rm -f /etc/nginx/sites-enabled/default  
ADD vhost.conf /etc/nginx/sites-available/default  
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Install swoole php extension  
RUN pecl install swoole  
ADD 20-swoole.ini /etc/php/7.0/fpm/conf.d/20-swoole.ini  
RUN ln -s /etc/php/7.0/fpm/conf.d/20-swoole.ini
/etc/php/7.0/cli/conf.d/20-swoole.ini  
  
# Add PHP FPM Pool config  
ADD fpm-pool.conf /etc/php/7.0/fpm/pool.d/www.conf  
RUN mkdir /run/php/  
  
# Install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/ && \  
ln -s /usr/local/bin/composer.phar /usr/local/bin/composer  
  
# Add start script  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
# Expose ports  
EXPOSE 80 9051  
  
# Start it  
ENTRYPOINT ["/start.sh"]  

