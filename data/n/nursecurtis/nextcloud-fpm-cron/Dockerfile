FROM nextcloud:fpm  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list \  
&& apt-get update && apt-get install -y \  
supervisor \  
cron \  
ffmpeg \  
libreoffice-writer \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/log/supervisord /var/run/supervisord && \  
echo "*/15 * * * * su - www-data -s /bin/bash -c \"php -f
/var/www/html/cron.php\""| crontab -  
  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]  

