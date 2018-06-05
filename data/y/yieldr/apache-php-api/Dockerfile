FROM yieldr/apache-php  
  
ENV CRON_VERSION 0.8.0  
ENV CRON_OS linux  
ENV CRON_ARCH amd64  
  
RUN set -x \  
&& apt-get update -y --no-install-recommends \  
&& apt-get install -y g++ make \  
&& pecl install grpc-1.4.6 \  
&& echo "extension=grpc.so" >> /etc/php5/cli/php.ini \  
&& pecl config-set php_ini /etc/php5/cli/php.ini \  
&& echo "extension=grpc.so" >> /etc/php5/apache2/php.ini \  
&& pecl config-set php_ini /etc/php5/apache2/php.ini \  
&& mkdir -p /home/code \  
&& ln -sf /home/code/web /var/www/code \  
&& chown www-data:www-data -R /home/code \  
&& curl -o /usr/bin/crond -sSL
https://github.com/alexkappa/crond/releases/download/v$CRON_VERSION/crond-$CRON_OS-$CRON_ARCH
\  
&& chmod +x /usr/bin/crond \  
&& curl -L https://github.com/FriendsOfPHP/PHP-CS-
Fixer/releases/download/v2.7.0/php-cs-fixer.phar -o php-cs-fixer \  
&& chmod a+x php-cs-fixer \  
&& mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
COPY vhost.conf /etc/apache2/sites-available/000-default.conf  
  
ADD docker-entrypoint.sh /  
  
ONBUILD ADD . /home/code  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["apachectl", "-D", "FOREGROUND"]  

