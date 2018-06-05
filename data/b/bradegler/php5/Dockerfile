FROM bradegler/nginx  
  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository -y ppa:ufirst/php5  
RUN apt-get update  
  
RUN apt-get -y install php5-fpm php5-mysql php-apc php5-imagick php5-imap
php5-mcrypt php5-curl php5-cli php5-gd php5-pgsql php5-sqlite php5-common php-
pear php5-json php5-redis  
RUN apt-get install -y redis-server memcached php5-memcache  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/  
RUN mv /usr/bin/composer.phar /usr/bin/composer  
  
RUN echo "<?php phpinfo(); ?>" > /tmp/phpinfo.php  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure supervisord to run fpm  
RUN echo "[program:php-fpm]" > /etc/supervisor/conf.d/php-fpm.conf && \  
echo "command = /usr/sbin/php5-fpm" >> /etc/supervisor/conf.d/php-fpm.conf &&
\  
echo "user = root" >> /etc/supervisor/conf.d/php-fpm.conf && \  
echo "autostart = true" >> /etc/supervisor/conf.d/php-fpm.conf  
  
# Set daemonize = no otherwise it restarts constantly under supervisord  
RUN sed -i -e 's/;daemonize = yes/daemonize = no/' /etc/php5/fpm/php-fpm.conf  
  
CMD ["/usr/bin/supervisord"]

