FROM tutum/apache-php  
  
ADD vhost.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN sed -i -e "s/short_open_tag = Off/short_open_tag = On/g"
/etc/php5/apache2/php.ini  
  
ADD . /var/www/html  

