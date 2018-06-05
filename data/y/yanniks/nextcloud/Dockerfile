FROM nextcloud:apache  
  
RUN apt-get update && apt-get install -y \  
supervisor \  
libsmbclient-dev \  
cron \  
&& pecl install smbclient \  
&& docker-php-ext-enable smbclient \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/log/supervisord /var/run/supervisord && \  
echo "*/15 * * * * su - www-data -s /bin/bash -c \"php -f
/var/www/html/cron.php\""| crontab -  
  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]  

