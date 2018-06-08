FROM milos/docker-centos-apache-php  
  
RUN export COMPOSER_HOME=/usr/local/composer && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
WORKDIR /var/www  
VOLUME ["/var/www"]  
  
ENTRYPOINT ["/usr/local/bin/composer"]  
  

