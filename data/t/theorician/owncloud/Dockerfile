FROM owncloud  
MAINTAINER theorician  
  
ADD default-ssl.conf /etc/apache2/sites-enabled  
RUN cp /etc/apache2/mods-available/ssl* /etc/apache2/mods-enabled  
RUN cp /etc/apache2/mods-available/socache_shmcb.load /etc/apache2/mods-
enabled  
  
EXPOSE 443  
VOLUME ["/config", "/mail", "/ssl"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]

