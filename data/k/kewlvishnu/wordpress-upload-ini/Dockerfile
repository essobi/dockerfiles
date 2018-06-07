FROM wordpress:latest  
  
RUN a2enmod rewrite expires headers deflate  
  
ADD uploads.ini /usr/local/etc/php/conf.d/  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

