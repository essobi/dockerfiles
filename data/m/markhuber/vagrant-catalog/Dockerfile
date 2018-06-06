FROM tutum/apache-php  
  
RUN apt-get update && apt-get install -yq git && rm -rf /var/lib/apt/lists/*  
  
RUN rm -rf /var/www/html && git clone https://github.com/vube/vagrant-catalog
/var/www/html  
  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
  
WORKDIR /var/www/html  
RUN composer update  
RUN mv config.php.dist config.php  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/run.sh"]

