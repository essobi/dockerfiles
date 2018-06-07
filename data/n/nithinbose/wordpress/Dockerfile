FROM wordpress:php7.1-apache  
  
# Add PHP Zip Archive extension  
RUN apt-get update \  
&& apt-get install -y zlib1g-dev cron \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install zip  
  
COPY uploads.ini /usr/local/etc/php/conf.d/  
COPY wp-config-sample.php /usr/src/wordpress/  
  
# Add crontab file in the cron directory  
COPY crontab /etc/cron.d/wp-cron  
# Give execution rights on the cron job  
RUN chmod 0644 /etc/cron.d/wp-cron  
  
COPY start.sh /usr/local/bin/  
ENTRYPOINT ["start.sh"]  

