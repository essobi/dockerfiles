FROM php:7.0-apache  
  
RUN apt-get update && \  
apt-get install -y git zlib1g-dev cron  
  
RUN docker-php-ext-install zip  
  
RUN curl https://getcomposer.org/composer.phar > /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer  
  
ADD . /satis  
ADD ./cron/* /etc/cron.d/  
  
RUN cd /satis && \  
composer install  
  
# Give us a file to write the cron too  
RUN touch /var/log/cron.log  
  
# Disable PHP in Apache, we're only serving static files  
RUN a2dismod php7  
  
# Enable mod_rewrite for our access control  
RUN a2enmod rewrite  
  
CMD bash /satis/bin/init.sh && tail -f /var/log/cron.log  

