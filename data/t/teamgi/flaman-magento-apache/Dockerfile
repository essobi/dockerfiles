FROM teamgi/flaman-php  
  
ADD ./001-vhost.conf /etc/apache2/sites-available/  
ADD ./002-magento-ssl.conf /etc/apache2/sites-available/  
  
RUN ln -s /etc/apache2/sites-available/001-vhost.conf /etc/apache2/sites-
enabled/  
RUN ln -s /etc/apache2/sites-available/002-magento-ssl.conf
/etc/apache2/sites-enabled/

