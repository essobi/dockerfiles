FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y software-properties-common language-
pack-en-base \  
&& LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install -y netcat mcrypt curl sendmail supervisor git php-redis
mcrypt php7.0 php7.0-cli \  
php7.0-common php7.0-curl php7.0-fpm php7.0-gd php7.0-intl php7.0-json
php7.0-mbstring \  
php7.0-mcrypt php7.0-mysql php7.0-opcache php7.0-readline php7.0-soap
php7.0-xml php7.0-zip \  
&& mkdir /run/php \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
# Make sure we're installing what we think we're installing!  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --snapshot \  
&& rm -f /tmp/composer-setup.*  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN sed -i -e 's/listen = \/run\/php\/php7.0-fpm.sock/listen = 0.0.0.0:9000/g'
/etc/php/7.0/fpm/pool.d/www.conf \  
&& sed -i -e 's/;daemonize = yes/daemonize = no/g' /etc/php/7.0/fpm/php-
fpm.conf \  
&& sed -i -e 's/;clear_env = no/clear_env = no/g'
/etc/php/7.0/fpm/pool.d/www.conf \  
&& sed -i -e 's/pm.max_children = 5/pm.max_children = 40/g'
etc/php/7.0/fpm/pool.d/www.conf \  
&& usermod -u 1000 www-data  
  
WORKDIR /var/app  
  
EXPOSE 9000  
  
CMD ["/usr/bin/supervisord"]

