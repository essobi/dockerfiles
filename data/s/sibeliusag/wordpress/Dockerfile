FROM wordpress:latest  
  
# Install unzip to handle plugins  
RUN apt-get update && apt-get install -y unzip rsync && rm -rf
/var/lib/apt/lists/*  
  
# Increase upload limit  
RUN touch /usr/local/etc/php/conf.d/upload-limit.ini \  
&& echo "upload_max_filesize = 32M" >> /usr/local/etc/php/conf.d/upload-
limit.ini \  
&& echo "post_max_size = 32M" >> /usr/local/etc/php/conf.d/upload-limit.ini  
  
# Enable additional headers for caching  
RUN a2enmod expires headers  
  
VOLUME /var/www/html  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

