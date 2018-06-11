FROM wordpress  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN chmod -R 777 /etc/apache2/  
RUN chmod -R 777 /var/lock/apache2/  
RUN chmod -R 777 /var/run/apache2/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["apache2-foreground"]  

