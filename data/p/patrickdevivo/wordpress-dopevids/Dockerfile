FROM wordpress:latest  
  
RUN a2enmod rewrite expires headers deflate  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

