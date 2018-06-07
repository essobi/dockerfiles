FROM php:7.1-alpine  
  
RUN apk add --no-cache \  
# Install OS level dependencies  
git zip unzip curl \  
libpng-dev libmcrypt-dev bzip2-dev icu-dev mariadb-client && \  
# Install PHP dependencies  
docker-php-ext-install pdo_mysql gd bz2 intl mcrypt pcntl  
  
# Add the SeAT crontab entry  
RUN touch crontab.tmp \  
&& echo '* * * * * php /var/www/seat/artisan schedule:run' > crontab.tmp \  
&& crontab -u www-data crontab.tmp \  
&& rm -rf crontab.tmp  
  
# Skip migrations and assets publishing for this  
# container as those are not needed. App container  
# has this covered.  
COPY startup.sh /root/startup.sh  
RUN chmod +x /root/startup.sh  
  
VOLUME "/var/www/seat"  
WORKDIR /var/www/seat  
  
ENTRYPOINT ["/bin/sh", "/root/startup.sh"]  

