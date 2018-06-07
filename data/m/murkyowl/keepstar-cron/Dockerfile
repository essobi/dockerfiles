FROM php:7.1-alpine  
  
RUN apk add --no-cache \  
# Install OS level dependencies  
git zip unzip curl \  
libpng-dev libmcrypt-dev bzip2-dev icu-dev mariadb-client && \  
# Install PHP dependencies  
docker-php-ext-install pdo_mysql gd bz2 intl mcrypt pcntl  
  
# Add the crontab entry  
RUN touch crontab.tmp \  
&& echo '0 */2 * * * php /var/www/Keepstar/cron.php' > crontab.tmp \  
&& crontab crontab.tmp \  
&& rm -rf crontab.tmp  
  
COPY startup.sh /root/startup.sh  
RUN chmod +x /root/startup.sh  
  
WORKDIR /var/www/Keepstar/  
  
ENTRYPOINT ["/bin/sh", "/root/startup.sh"]  

