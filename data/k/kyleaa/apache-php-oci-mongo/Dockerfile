FROM davidgaya/apache-php-oci:latest  
  
RUN printf "\n" | pecl install mongo  
RUN apt-get install -y php5-mcrypt  
RUN apt-get clean -y  
  
RUN echo "extension=mcrypt.so" > /etc/php5/apache2/conf.d/50-mcrypt.ini  
RUN echo "extension=mongo.so" > /etc/php5/apache2/conf.d/40-mongo.ini  
  
RUN curl https://phar.phpunit.de/phpunit.phar > /tmp/phpunit.phar  
RUN chmod +x /tmp/phpunit.phar  
RUN mv /tmp/phpunit.phar /usr/local/bin/phpunit  
  
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load  

